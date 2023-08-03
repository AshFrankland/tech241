story1 = {
    'start': 'The Code won\'t compile!!!',
    'middle': 'Intense debugging montage',
    'end': 'Everything works, time to commit to Git'
}

print(story1)
print(type(story1))
print(story1.keys())
print(story1.values())
print(story1['start'])
print(story1['middle'])
print(story1['end'])

story1['hero'] = 'The Setup Wizard'

print(story1)
