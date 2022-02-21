# Item attributes default values (here they are constant, however they can be taken from a confguration file/database in real life)

DEFAULT_STEP = -1
DEFAULT_STEP_TABLE = None
DEFAULT_QUALITY_DATE_PASSED = None
DEFAULT_STEP_DATE_PASSED = -2
DEFAULT_MIN_QUALITY = 0
DEFAULT_MAX_QUALITY = 50
DEFAULT_ALLOW_SALE = True



class Item:

    def __init__(self, item):
        self.step = item["step"] if "step" in item else DEFAULT_STEP
        self.step_table = item["step_table"] if "step_table" in item else DEFAULT_STEP_TABLE
        self.min_quality = item["min_quality"] if "min_quality" in item else DEFAULT_MIN_QUALITY
        self.max_quality = item["max_quality"] if "max_quality" in item else DEFAULT_MAX_QUALITY
        self.allow_sale = item["allow_sale"] if "allow_sale" in item else DEFAULT_ALLOW_SALE
        self.quality_date_passed = item["quality_date_passed"] if "quality_date_passed" in item else DEFAULT_QUALITY_DATE_PASSED
        self.step_date_passed = item["step_date_passed"] if "step_date_passed" in item else DEFAULT_STEP_DATE_PASSED
