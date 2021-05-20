# --------------
# STEP 1:
print("\t\t\t Step = 1")
class_1 = ['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class_2 = ['Hilary Mason','Carla Gentry','Corinna Cortes']

new_class = class_1 + class_2
print(new_class)

new_class.append('Peter Warden')
print(new_class)

new_class.remove('Carla Gentry')
print(new_class)


# STEP 2:
print("\n\n\t\t\t Step = 2")
courses = {'Math':65 , 'English':70 , 'History':80 , 'French':70 , 'Science':60}

total = courses['Math'] + courses['English'] + courses['History'] + courses['French'] + courses['Science']
print(total)

percentage = (total/500)*100
print(percentage)


# STEP 3:
print("\n\n\t\t\t Step = 3")
mathematics = {'Geoffrey Hinton':78 , 'Andrew Ng':95 , 'Sebastian Raschka':65 , 'Yoshua Benjio':50 , 'Hilary Mason':70 , 'Corinna Cortes':66 , 'Peter Warden':75}

topper = max(mathematics , key = mathematics.get)
print(topper)


# STEP 4:
print("\n\n\t\t\t Step = 4")
first_name = topper.split()[0]
last_name = topper.split()[1]

full_name = last_name + " " + first_name
certificate_name = full_name.upper()
print(certificate_name)



