import re

with open('data.html', 'r') as myfile:
    data=myfile.read().replace('\n', '')
    
result=re.findall(r'<td>\w+</td>\s<td>(\w+)</td>\s<td>(\w+)</td>',data)
print(result)