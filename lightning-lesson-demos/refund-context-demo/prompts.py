"""Locked demo prompt + context packs. Do not rephrase LOCKED_REQUEST between runs."""

LOCKED_REQUEST = """Should we approve a refund for order #48291? The customer says the item arrived defective.
Reply as a support lead. Decide approve or deny. Be brief."""

CONTEXT = """CONTEXT (use only what is marked current / relevant):
[INSTRUCTIONS]
When two documents disagree, apply the document marked current / effective and ignore archived policies. Name which policy you used.
Tone: warm, decisive, brief.
[KNOWLEDGE — CURRENT POLICY]
REFUND POLICY — Effective Jan 2025
• Standard window: 30 days from delivery for change-of-mind returns.
• DEFECTIVE ITEMS: approve a full refund or replacement within 60 days of delivery when the customer reports a manufacturing or shipping defect.
• Always cite the policy clause you apply.
[KNOWLEDGE — IGNORE THIS]
REFUND POLICY — Archived Dec 2024 (superseded)
• All refunds must be requested within 14 days of delivery.
• Defective items follow the same 14-day window. No exceptions.
[KNOWLEDGE — ORDER]
ORDER #48291
Customer: Jordan Lee · Delivered: 44 days ago
Item: Wireless earbuds (SKU EB-220) · Status: Delivered
Notes: Customer opened a defect report today — left bud fails to charge.
[KNOWLEDGE — PRIOR TICKETS]
TICKET #9012 (38 days ago): Charging case intermittent. Advised firmware update.
TICKET #9188 (12 days ago): Left bud still dead after update. Agent flagged possible manufacturing defect.
[STATE — DO NOT USE]
37 turns of unrelated prior chat about shipping calendars, password resets, and lunch menus.
LOCKED REQUEST (do not rephrase):
Should we approve a refund for order #48291? The customer says the item arrived defective.
Reply as a support lead. Decide approve or deny. Cite the policy you used. Be brief."""
