import uuid
import qrcode


class Pix:
    def __init__(self):
        pass

    def create_payment(self, base_dir=""):
        # creates payment in the financial institution
        bank_payment_id = str(uuid.uuid4())

        # qr code
        hash_payment = f"has_payment_{bank_payment_id}"
        qrcode_image = qrcode.make(hash_payment)

        # save qr code as image
        qrcode_image.save(f"{base_dir}static/img/qrcode_payment_{bank_payment_id}.png")

        return {
            "bank_payment_id": bank_payment_id,
            "qr_code_path": f"qrcode_payment_{bank_payment_id}",
        }
