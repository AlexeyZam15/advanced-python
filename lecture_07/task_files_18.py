text = ['Lorem ipsum dolor sit amet, consectetur adipisicingelit.',
        'Consequatur debitis explicabo laboriosam sint suscipittemporibus veniam?',
        'Accusantium alias amet fugit iste neque non odit quiasaepe totam velit?', ]
with open('new_data.txt', 'a', encoding='utf-8') as f:
    for line in text:
        res = f.write(f'{line}\n')
        print(f'{res = }\n{len(line) = }')
