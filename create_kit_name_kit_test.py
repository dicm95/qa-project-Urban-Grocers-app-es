import sender_stand_request
import data

def get_kit_body(kit_name):
    current_kit_body = data.kit_body.copy()
    current_kit_body['name'] = kit_name
    return current_kit_body

# Preparación pruebas positivas
def positive_assert(kit_name):
    kit_body = get_kit_body(kit_name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body)

    assert kit_response.status_code == 201
    assert kit_response.json()['name'] == kit_name

# Preparación pruebas negativas
def negative_assert_code_400(kit_name):
    kit_body = get_kit_body(kit_name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body)

    assert kit_response.status_code == 400

# Preparación prueba 8
def negative_assert_no_name(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body)

    assert response.status_code == 400

#Prueba 1. El número permitido de caracteres (1):
def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert(data.kit_body_name_test_one_character)

#Prueba 2. El número permitido de caracteres (511):
def test_create_kit_511_letter_in_name_get_success_response():
    positive_assert(data.kit_body_name_test_511_character)

#Prueba 3. El número de caracteres es menor que la cantidad permitida (0):
def test_create_kit_empty_name_get_error_response():
    negative_assert_code_400(data.kit_body_name_test_empty_name)

#Prueba 4. El número de caracteres es mayor que la cantidad permitida (512):
def test_create_kit_512_letter_in_name_get_error_response():
    negative_assert_code_400(data.kit_body_name_test_512_character)

#Prueba 5. Se permiten caracteres especiales:
def test_create_kit_has_special_symbol_in_name_get_success_response():
    positive_assert(data.kit_body_name_test_special_character)

#Prueba 6. Se permiten espacios:
def test_create_kit_has_space_in_name_get_success_response():
    positive_assert(data.kit_body_name_test_with_space)

#Prueba 7. Se permiten números:
def test_create_kit_has_number_in_name_get_success_response():
    positive_assert(data.kit_body_name_test_has_numbers)

#Prueba 8. El parámetro no se pasa en la solicitud:
def test_create_kit_no_name_get_error_response():
    kit_body = data.kit_body.copy()
    kit_body.pop('name')
    negative_assert_no_name(kit_body)

#Prueba 9. Se ha pasado un tipo de parámetro diferente (número):
def test_create_kit_different_parameter_get_error_response():
    negative_assert_code_400(data.kit_body_name_test_different_parameter)