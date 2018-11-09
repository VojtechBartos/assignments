from assignments.transformation import Transformation


def test_input_without_company():
    data = [
        {"key": "firstname", "value": "vojta"},
        {"key": "username", "value": "vojta"},
        {"key": "lastname", "value": "bartos"},
        {"key": "address", "value": "Kostelec nad Orlici"},
        {"key": "city"},
        {"key": "zipzode", "value": None},
        {"key": "firstname", "value": "pavel"},
        {"key": "company", "value": "apple"}
    ]
    output = [
        ('address', 'Kostelec nad Orlici'),
        ('company', 'apple'),
        ('firstname', 'pavel'),
        ('lastname', 'bartos'),
        ('username', 'vojta')
    ]
    transformation = Transformation()
    transformation_output = transformation.execute(data)
    assert len(transformation_output) == len(output)
    assert transformation_output == output