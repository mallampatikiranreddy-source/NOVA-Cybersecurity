# NOVA Cybersecurity
# AI-Powered Threat Detection and Risk Assessment System
#
# Current version: Rule-based prototype.
# Machine learning will be added in a future version.

print("=" * 50)
print("              NOVA CYBERSECURITY")
print("=" * 50)
print("AI-Powered Threat Detection and Risk Assessment System")
print("")

# Login history
login_history = []

while True:

    print("")
    print("-" * 50)
    print("NEW LOGIN ANALYSIS")
    print("-" * 50)

    # Get login information
    device = input(
        "Is this a new device? (yes/no): "
    ).strip().lower()

    location = input(
        "Is this an unusual location? (yes/no): "
    ).strip().lower()

    while True:
        try:
            failed_attempts = int(
                input("How many failed login attempts? ")
            )

            if failed_attempts < 0:
                print("Please enter a number 0 or greater.")
                continue

            break

        except ValueError:
            print("Please enter a valid whole number.")

    print("")
    print("Information received successfully!")

    # Calculate risk score
    risk_score = 0

    if device == "yes":
        risk_score += 30

    if location == "yes":
        risk_score += 40

    if failed_attempts >= 5:
        risk_score += 30

    # Keep risk score between 0 and 100
    risk_score = min(risk_score, 100)

    # Determine risk level
    if risk_score <= 30:
        risk_level = "LOW"

    elif risk_score <= 70:
        risk_level = "MEDIUM"

    else:
        risk_level = "HIGH"

    # Determine alert level
    if risk_score >= 80:
        alert_level = "CRITICAL"

    elif risk_score >= 50:
        alert_level = "WARNING"

    else:
        alert_level = "SAFE"

    # Determine security action
    if risk_score >= 80:
        action = "LOGIN BLOCKED"

    elif risk_score >= 50:
        action = "VERIFICATION REQUIRED"

    else:
        action = "LOGIN ALLOWED"

    # Save login attempt
    login_record = {
        "device": device,
        "location": location,
        "failed_attempts": failed_attempts,
        "risk_score": risk_score,
        "risk_level": risk_level,
        "alert_level": alert_level,
        "action": action
    }

    login_history.append(login_record)

    # Display security report
    print("")
    print("=" * 50)
    print("              NOVA SECURITY REPORT")
    print("=" * 50)

    print("Risk Score:", risk_score, "/ 100")
    print("Risk Level:", risk_level)
    print("Alert Level:", alert_level)
    print("Security Action:", action)

    if risk_score >= 70:
        print("WARNING: Suspicious login detected!")

    else:
        print("Login appears normal.")

    print("=" * 50)

    # Ask for another login
    another = input(
        "Analyze another login? (yes/no): "
    ).strip().lower()

    if another != "yes":
        break


# Display login history
print("")
print("=" * 50)
print("              NOVA LOGIN HISTORY")
print("=" * 50)

for number, login in enumerate(login_history, start=1):

    print("")
    print("Login Attempt:", number)
    print("Risk Score:", login["risk_score"])
    print("Risk Level:", login["risk_level"])
    print("Alert Level:", login["alert_level"])
    print("Security Action:", login["action"])

print("")
print("Total Login Attempts:", len(login_history))
print("=" * 50)
print("NOVA analysis completed.")
print("=" * 50)
