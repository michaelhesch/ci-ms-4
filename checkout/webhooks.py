import json
import stripe
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from checkout.webhook_handler import StripeWHHandler


@require_POST
@csrf_exempt
def webhook(request):
    # Configuration
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # Webhook data
    payload = request.body
    event = None

    try:
        event = stripe.Event.construct_from(
            json.loads(payload), wh_secret, stripe.api_key,
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except Exception as e:
        # Catch any remaining errors
        return HttpResponse(content=e, status=400)

    # Set up the webhook handler
    handler = StripeWHHandler(request)

    # Map webhook events to correct functions
    event_map = {
        'payment_intent.succeeded': handler.handle_payment_intent_succeeded,
        'payment_intent.payment_failed': handler.handle_payment_intent_failed
    }

    # Get webhook type
    event_type = event['type']

    # If a handler exists, select it from the map
    # Otherwise, use generic handler
    event_handler = event_map.get(event_type, handler.handle_event)

    # Call the event handler based on event and return
    response = event_handler(event)
    return response
