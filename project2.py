import csv


def write_into_csv(info_list):
    with open("student_info.csv", 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell() == 0:
            writer.writerow(["Name", "Age", "Contact_Number", "Email_Id"])
        writer.writerow(info_list)


if __name__ == '__main__':
    condition = True
    student_num = 1
    while condition:
        student_info = input(
            "enter the student information for student #{} in the following format[Name Age Contact_Number Email_Id] : ".format(student_num))

        student_info_list = student_info.split(' ')
        print("\nThe entered information is : \nName:{}\nAge:{}\nContact_Number:{}\nEmail_Id:{}\n".
              format(student_info_list[0], student_info_list[1], student_info_list[2], student_info_list[3]))
        choice_check = input("Recheck your information if its correct, yes/no: ")
        if choice_check == "yes":
            write_into_csv(student_info_list)

            _check = input("Enter yes/no if you want to proceed further or not : ")
            if _check == "yes":
                condition = True
                student_num+=1
            elif _check == "no":
                condition = False
        else:
            print("Please Re-enter")
