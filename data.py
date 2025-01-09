headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {auth_token}"
    }

user_body = {
    "firstName": "Daniela",
    "phone": "+34692670038",
    "address": "Barcelona, España"
}

kit_body = {
  "name": "Nombre"
}

kit_body_name_test_one_character = "a"

kit_body_name_test_511_character = "Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd" \
          "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd" \
          "abcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd" \
          "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd" \
          "abcdabcdabcdabcdabcdabcdabcdabC"

kit_body_name_test_empty_name = ""

kit_body_name_test_512_character = "Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd" \
            "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd" \
            "abcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd" \
            "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd" \
            "abcdabcdabcdabcdabcdabcdabcdabcD"

kit_body_name_test_special_character = "!#@?"

kit_body_name_test_with_space = " A Aaa "

kit_body_name_test_has_numbers = "123"

kit_body_name_test_different_parameter = 123