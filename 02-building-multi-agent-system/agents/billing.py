billing_assistant = {
    "id": "Assistant_BillingAssistant",
    "name": "Billing Support",
    "description": """Call this if:
        - Customer wants to check their current balance
        - Customer needs information about past invoices
        - Customer has questions about charges
        DO NOT CALL IF:
        - Technical support needed
        - Sales inquiries""",
    "system_message": """You are a billing support agent handling customer inquiries about balances and invoices.
    Keep sentences short and simple, suitable for voice conversation.
    
    Your tasks:
    - Check current outstanding balances
    - Explain any international call overcharges
    - Provide historical invoice information
    - Help customers understand their charges
    
    Make sure to:
    - Be professional and empathetic
    - Verify customer identity before sharing details
    - Explain charges clearly
    - Note that international calls may cause higher than usual charges""",
    "tools": [
        {
            "name": "check_outstanding_balance",
            "description": "Check customer's current outstanding balance and any overcharges from international calls",
            "parameters": {
                "type": "object",
                "properties": {"account_id": {"type": "string"}},
                "required": ["account_id"],
            },
            "returns": lambda input: {
                "balance": "€80.75",
                "international_calls_charge": "€45.50",
                "due_date": "2025-02-01",
            },
        },
        {
            "name": "get_monthly_invoice",
            "description": "Get the invoice amount for a specific month",
            "parameters": {
                "type": "object",
                "properties": {
                    "account_id": {"type": "string"},
                    "month": {
                        "type": "string",
                        "description": "Month in YYYY-MM format",
                    },
                },
                "required": ["account_id", "month"],
            },
            "returns": lambda input: {
                "total_amount": "€85.25",
                "base_charges": "€40.00",
                "usage_charges": "€45.25",
                "statement_date": f"{input['month']}-15",
            },
        },
    ],
}
