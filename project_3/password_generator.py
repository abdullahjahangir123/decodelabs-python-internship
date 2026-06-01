import math
import secrets
import string


class EnterprisePasswordGenerator:

    def __init__(self):
        # Professional character pooling using standard library
        self.letters = string.ascii_letters
        self.digits = string.digits
        self.punctuation = string.punctuation
        self.character_pool = self.letters + self.digits + self.punctuation
        self.pool_size = len(self.character_pool)

        # NIST 2024 Guidelines: Common compromised passwords to blocklist
        self.blocklist = [
            "password123",
            "12345678",
            "admin123",
            "welcome2026",
            "abcd123",
        ]

    def validate_length(self, length_input):
        """Phase 1: Input Validation (NIST 2024 Standards)"""
        try:
            length = int(length_input)
            if length < 15:
                print(
                    "[!] Warning: NIST guidelines recommend a minimum of 15 characters for high security."
                )
                if length < 8:
                    raise ValueError(
                        "Password length too short! Minimum allowed is 8."
                    )
            if length > 64:
                raise ValueError(
                    "Password length too long! Maximum allowed is 64."
                )
            return length
        except ValueError as e:
            print(f"[-] Validation Error: {e}")
            return None

    def generate_password(self, length):
        """Phase 2: Core Processing Engine (Secure & Optimized)"""
        while True:
            # O(N) Optimization using list comprehension and ''.join()
            # Cryptographically secure randomness using secrets.choice()
            password_list = [
                secrets.choice(self.character_pool) for _ in range(length)
            ]
            password = "".join(password_list)

            # NIST Screening: Check against blocklist
            if not any(
                blocked in password.lower() for blocked in self.blocklist
            ):
                return password

    def calculate_entropy(self, length):
        """Phase 3: Mathematical Security Provision"""
        # Formula: E = L * log2(R)
        entropy = length * math.log2(self.pool_size)
        return round(entropy, 2)


# --- Execution / IPO Flow ---
if __name__ == "__main__":
    print("=== DecodeLabs Enterprise Password Generator ===")
    generator = EnterprisePasswordGenerator()

    # 1. Input Phase
    user_input = input("Enter password length (15 - 64): ")

    # Validation
    validated_length = generator.validate_length(user_input)

    if validated_length:
        # 2. Process Phase
        secure_password = generator.generate_password(validated_length)
        entropy_bits = generator.calculate_entropy(validated_length)

        # 3. Output Phase
        print("\n" + "=" * 40)
        print(f"[+] Generated Password : {secure_password}")
        print(f"[+] Information Entropy: {entropy_bits} bits")

        # Strength Assessment
        if entropy_bits >= 128:
            print("[+] Security Status    : Cryptographically Ultra-Strong")
        elif entropy_bits >= 80:
            print("[+] Security Status    : Strong")
        else:
            print("[-] Security Status    : Weak (Increase length)")
        print("=" * 40)
