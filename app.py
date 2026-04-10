import json

def build_html(fact: dict) -> str:
    return f"""
    <div style='font-family: Arial, sans-serif; max-width: 640px; margin: 0 auto; color: #17202a;'>
      <p style='font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #4b5563;'>Ireland in May · Daily Fact</p>
      <h1 style='font-size: 28px; margin-bottom: 8px;'>{fact['title']}</h1>
      <p style='font-size: 18px; line-height: 1.6;'>{fact['fact']}</p>

      <div style='background: #f3f4f6; border-radius: 16px; padding: 16px; margin: 20px 0;'>
        <h2 style='font-size: 16px; margin: 0 0 8px;'>Why it matters in May</h2>
        <p style='margin: 0; line-height: 1.6;'>{fact['why_may_matters']}</p>
      </div>

      <div style='margin: 20px 0;'>
        <h2 style='font-size: 16px; margin-bottom: 8px;'>Try this</h2>
        <p style='line-height: 1.6;'>{fact['traveler_tip']}</p>
      </div>

      <div style='margin: 20px 0;'>
        <h2 style='font-size: 16px; margin-bottom: 8px;'>Source note</h2>
        <p style='font-size: 14px; color: #4b5563; line-height: 1.6;'>{fact['source_note']}</p>
      </div>

      <hr style='border: none; border-top: 1px solid #e5e7eb; margin: 24px 0;'>
      <p style='font-size: 12px; color: #6b7280;'>Generated automatically. Edit the prompt or email template anytime.</p>
    </div>
    """


def send_email(to_email: str, fact: dict):
    subject = f"Ireland in May: {fact['title']}"
    html = build_html(fact)

    resend.Emails.send(
        {
            "from": FROM_EMAIL,
            "to": [to_email],
            "subject": subject,
            "html": html,
        }
    )


def main():
    now = datetime.now(timezone.utc)
    day_number = int(now.strftime("%j"))
    fact = generate_fact(day_number=day_number)
    subscribers = load_subscribers()

    for subscriber in subscribers:
        send_email(subscriber["email"], fact)
        print(f"Sent to {subscriber['email']}")


if __name__ == "__main__":
    main()
