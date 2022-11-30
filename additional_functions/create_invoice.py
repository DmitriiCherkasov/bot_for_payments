from yookassa import Configuration, Payment
from additional_functions.get_from_env_function import get_from_env


def create_invoice(price: int, order: str, return_data=None):
    Configuration.account_id = get_from_env("SHOP_ID")
    Configuration.secret_key = get_from_env("TOKEN_YOOKASSA")

    payment = Payment.create({
        "amount": {
            "value": price,
            "currency": "RUB"
        },
        "confirmation": {
            "type": "redirect",
            "return_url": "https://t.me/Nutrigenom_payments_bot"
        },
        "capture": True,
        "description": order,
        "metadata": {
          "return_data":return_data
        }})
    return payment.confirmation.confirmation_url
