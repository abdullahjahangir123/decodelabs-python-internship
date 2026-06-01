# 🛡️ Enterprise Random Password Generator

Powered by **DecodeLabs** | Batch: 2026  
*Developed by: Abdullah*

An enterprise-grade, cryptographically secure password generation tool built following the **NIST 2024 (SP 800-63-4) Security Guidelines** and structured on the **Input-Process-Output (IPO)** architecture.

---

## 📌 Project Overview & Purpose

Yeh project sirf ek aam random character generator nahi hai, balki ise enterprise-level backend security standards par design kiya gaya hai. Real-world applications mein jab users naya account banate hain ya cloud platforms API Keys generate karte hain, to wahan isi tarah ki advanced logic ka istemal hota hai.

### Key Learning Outcomes:
- **Module Integration:** Python ki built-in core security libraries (`secrets`, `string`, `math`) ka advanced istemal.
- **Cryptographic Integrity:** Standard randomizer ke bajaye OS-level hardware noise (entropy) ka use.
- **Memory Optimization:** Linear time complexity $O(N)$ ke sath memory allocation ko optimize karna using `"".join()`.

---

## ⚙️ Architectural Scaffold (IPO Model)

Is software ko mukammal taur par clean, object-oriented aur secure banane ke liye 3 main phases mein divide kiya gaya hai:



[Image of Input-Process-Output model diagram]


1. **Phase 1: Input & Data Validation (Gatekeeper)**
   - User se password ki required length input li jati hai.
   - Strict validation lagayi gayi hai taake agar user text (alphabets) ya out-of-range number enter kare, to system crash na ho (`try-except` handling).
   - **NIST 2024 Compliance:** High-security contexts ke liye minimum **15 characters** aur passphrases ke liye maximum **64 characters** ki length strictly enforce ki gayi hai.

2. **Phase 2: Processing Engine (The Transformer)**
   - **Character Pooling:** `string` module ke zariye uppercase letters, lowercase letters, digits, aur punctuation symbols ka ek automated secure pool banaya jata hai.
   - **Cryptographic Randomness:** Mersenne Twister algorithm (`import random`) jo ke predictable hota hai, use block karke Python ka **`secrets.choice()`** use kiya gaya hai jo non-predictable data generate karta hai.
   - **Screening:** Generated password ko common/compromised passwords ki list (`blocklist`) se screen kiya jata hai.

3. **Phase 3: Output Delivery (Security Provision)**
   - Generated token ko safely display kiya jata hai.
   - **Information Entropy Calculation:** Mathematically password ki absolute strength bits mein calculate ki jati hai using the formula:
     $$E = L \times \log_2(R)$$
     *(Jahan $L$ password ki length hai aur $R$ character pool ka size hai).*

---

## 🚀 How To Run The Project

### Prerequisites
Aap ke computer mein **Python 3.6+** install hona chahiye. Kisi bhi external third-party library (`pip install`) ki zaroorat nahi hai.

### Step-by-Step Execution
1. Clone or download this repository to your local machine.
2. Open your Terminal / Command Prompt and navigate to the project directory:
   ```bash
   cd path/to/project-3
