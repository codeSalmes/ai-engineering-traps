# verify_thermal_math.py
# Run this locally to prove the steady-state math and the power limit trap.

def calculate_steady_state_thermal():
    I = 15.0; Rds_25 = 0.008; alpha = 0.005
    Ta = 80.0; Rth_ja = 1.5 + 25.0
    max_Tj = 175.0; max_P = 2.5

    print("--- Initial Nominal Calculation ---")
    P_nominal = (I**2) * Rds_25
    print(f"Nominal Power at 25C: {P_nominal:.2f} W")

    print("\n--- Solving Thermal Feedback Loop ---")
    Tj_guess = Ta
    for i in range(100):
        Rds_actual = Rds_25 * (1 + alpha * (Tj_guess - 25.0))
        P_actual = (I**2) * Rds_actual
        Tj_new = Ta + (P_actual * Rth_ja)
        if abs(Tj_new - Tj_guess) < 0.0001:
            break
        Tj_guess = Tj_new

    print(f"Steady-State Junction Temp: {Tj_new:.2f} C")
    print(f"Actual Power Dissipation:   {P_actual:.2f} W")

    print("\n--- Checking Datasheet Limits ---")
    status = "PASS"
    if Tj_new > max_Tj:
        print(f"[FAIL] Temp exceeds Max")
        status = "FAIL"
    if P_actual > max_P:
        print(f"[FAIL] Power ({P_actual:.2f}W) exceeds Max ({max_P}W)")
        status = "FAIL"

    print(f"\nFinal Status: {status}")

if __name__ == "__main__":
    calculate_steady_state_thermal()
