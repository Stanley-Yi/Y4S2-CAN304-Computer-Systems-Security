import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import new_rsa
import RSA_GUI
import improve_by_Ascii as iba
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import datetime
from brute_force import bruteRSA
from binascii import hexlify


global generate_prime_type
global plaintext_process_type
global method_type

global plain_text
global plain_text_ascii
global cipher_text
global decryption_text
global rsa
global keys
global python_ciphertext
global python_public_key
global python_private_key

def big_prime_click_success():
    global generate_prime_type
    ui.prime_chosen_text.setPlainText("Big prime generation")
    generate_prime_type = "big_prime"


def improve_by_ascii_button_click_success():
    global plaintext_process_type
    ui.plaintext_process_chosen_text.setPlainText("Improve by ascii")
    plaintext_process_type = "ascii"


def no_treatment_button_click_success():
    global plaintext_process_type
    ui.plaintext_process_chosen_text.setPlainText("No treatment")
    plaintext_process_type = "no_treatment"


def quick_power_button_click_success():
    global method_type
    ui.method_chosen_text.setPlainText("Quick power")
    method_type = "quick_power"


def crt_button_click_success():
    global method_type
    ui.method_chosen_text.setPlainText("Chinese remainder theorem")
    method_type = "crt"


def encryption_button_click_success():
    global plain_text
    global keys
    global cipher_text
    global python_ciphertext
    global python_public_key
    global python_private_key

    start_time = datetime.datetime.now()

    plain_text = ui.plain_text.toPlainText()
    text = plain_text
    if plaintext_process_type == "ascii":
        text = str(iba.improve_encryption(text))
        plain_text = text
    elif generate_prime_type == "python":
        private_key = RSA.generate(1024)
        public_key = private_key.publickey()
        cipher = PKCS1_OAEP.new(public_key)
        text = text.encode("utf-8")
        ciphertext = cipher.encrypt(text)
        ui.cipher_text.setPlainText(str(ciphertext))
        python_ciphertext = ciphertext
        python_public_key = public_key
        python_private_key = private_key

        end_time = datetime.datetime.now()
        time_length = end_time - start_time
        ui.encryption_time_text.setPlainText(str(time_length))

        return

    rsa = new_rsa.RSA()
    c = []
    keys = rsa.generate_update()

    for i in range(len(text)):
        c.append(rsa.encrypt_update(m=ord(text[i]), e=keys['e'], n=keys['n']))

    cipher_text = c
    cc = "".join(str(c))
    ui.cipher_text.setPlainText(cc)

    end_time = datetime.datetime.now()
    time_length = end_time - start_time
    ui.encryption_time_text.setPlainText(str(time_length))


def decryption_button_click_success():
    global cipher_text
    global decryption_text
    global keys
    global plaintext_process_type
    global method_type
    global plain_text
    global python_ciphertext
    global python_public_key
    global python_private_key

    start_time = datetime.datetime.now()

    if method_type == "python":
        cipher = PKCS1_OAEP.new(python_private_key)
        plaintext = cipher.decrypt(python_ciphertext)
        plaintext = str(plaintext, 'utf-8')
        ui.decryption_text.setPlainText(plaintext)

        end_time = datetime.datetime.now()
        time_length = end_time - start_time
        ui.decryption_time_text.setPlainText(str(time_length))

        return
    text = plain_text
    c, m = [], []
    rsa = new_rsa.RSA()
    c = cipher_text

    p, q, dp, dq, qinv, d, n = keys['p'], keys['q'], keys['dp'], keys['dq'], keys['qinv'], keys['d'], keys['n']
    if method_type == "quick_power":
        for i in range(len(text)):
            # m.append(chr(rsa.decrypt_update(c=c[i], d=local_keys['d'], n=local_keys['n'])))
            m.append(chr(rsa.decrypt_update(c[i], d, n)))
    elif method_type == "crt":
        for i in range(len(text)):
            # m.append(chr(rsa.crt(info=c[i], p=local_keys['p'], q=local_keys['q'], dp=local_keys['dp'], dq=local_keys['dq'], qinv=local_keys['qinv'])))
            m.append(chr(rsa.crt(c[i], p, q, dp, dq, qinv)))
    ming = "".join(m)

    if plaintext_process_type == "ascii":
        ming = iba.improve_decryption(ming)
    ui.decryption_text.setPlainText(ming)
    decryption_text = ming

    end_time = datetime.datetime.now()
    time_length = end_time - start_time
    ui.decryption_time_text.setPlainText(str(time_length))


def refresh_button_click_success():
    generate_prime_type = ""
    plaintext_process_type = ""
    method_type = ""
    plain_text = ""
    cipher_text = ""
    decryption_text = ""

    ui.prime_chosen_text.setPlainText("")
    ui.plaintext_process_chosen_text.setPlainText("")
    ui.method_chosen_text.setPlainText("")
    ui.plain_text.setPlainText("")
    ui.cipher_text.setPlainText("")
    ui.decryption_text.setPlainText("")
    ui.encryption_time_text.setPlainText("")
    ui.decryption_time_text.setPlainText("")
    # ui.brute_force_time_text.setPlainText("")


def python_rsa_button_click_success():
    global generate_prime_type
    global plaintext_process_type
    global method_type
    generate_prime_type = "python"
    plaintext_process_type = "python"
    method_type = "python"

    ui.prime_chosen_text.setPlainText("Python RSA")
    ui.plaintext_process_chosen_text.setPlainText("Python RSA")
    ui.method_chosen_text.setPlainText("Python RSA")


# def brute_force_button_click_success():
#     global keys
#     global method_type
#     global plaintext_process_type
#     global plain_text
#
#     start_time = datetime.datetime.now()
#
#     try:
#         bf_d = bruteRSA(keys['n'], keys['e'])
#     except:
#         ui.brute_force_time_text.setPlainText("Brute force failed")
#     end_time = datetime.datetime.now()
#     time_length = end_time - start_time
#     ui.brute_force_time_text.setPlainText(str(time_length))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = RSA_GUI.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    generate_prime_type = None
    plaintext_process_type = None
    method_type = None

    plain_text = None
    plain_text_ascii = None
    cipher_text = None
    decryption_text = None
    rsa = None
    keys = None
    python_ciphertext = None
    python_public_key = None
    python_private_key = None
    # function button
    ui.big_prime_generation_button.clicked.connect(big_prime_click_success)
    ui.improve_by_ascii_button.clicked.connect(improve_by_ascii_button_click_success)
    ui.no_treatment_button.clicked.connect(no_treatment_button_click_success)
    ui.quick_power_button.clicked.connect(quick_power_button_click_success)
    ui.crt_button.clicked.connect(crt_button_click_success)
    ui.python_rsa_button.clicked.connect(python_rsa_button_click_success)

    # action button
    ui.refresh_button.clicked.connect(refresh_button_click_success)
    ui.encryption_button.clicked.connect(encryption_button_click_success)
    ui.decryption_button.clicked.connect(decryption_button_click_success)
    # ui.brute_force_button.clicked.connect(brute_force_button_click_success)

    sys.exit(app.exec_())