import csv


def copy(file, new_file):
    """Takes in a file name and a new file name and copies the contents of
    the first file to the second file.

    Args:
        file (str): name of old file
        new_file (str): name of new file
    """
    with open(file) as file, open(new_file, 'w') as new:
        text = file.read()
        new.write(text)


def copy_and_reverse(old_file, new_file):
    """Takes in a file name and a new file name and copies the reversed
    contents of the first file to the second file.

    Args:
        file (str): name of old file
        new_file (str): name of new file
    """
    with open(old_file) as old, open(new_file, 'w') as new:
        text = old.read()
        new.write(text[::-1])


def update_users(old_first, old_last, new_first, new_last):
    """Takes in an old first name, an old last name, a new first name,
    and a new last name.

    Updates the file so that any user whose first
    and last names match the old first and last names are updated to
    the new first and last names.

    Args:
        old_first (str): old first name
        old_last (str): old last name
        new_first (str): new first name
        new_last (str): new last name

    Returns:
        str: updated users info
    """
    with open("users.csv") as csvf:
        csv_reader = csv.reader(csvf)
        rows = list(csv_reader)

        count = 0
        with open("users.csv", "w") as csvf:
            csv_writer = csv.writer(csvf)
            for row in rows:
                if row[0] == old_first and row[1] == old_last:
                    csv_writer.writerow([new_first, new_last])
                    count += 1
                else:
                    csv_writer.writerow(row)

        return 'Updated users: {}'.format(count)


def delete_users(first, last):
    """Takes in a first name and a last name.

    Updates the users.csv file so that any user whose first and last names
    match the inputs are removed.

    Args:
        first (str): first name of user
        last (str): last name of user

    Returns:
        str: count of how many users were deleted
    """

    with open("users.csv") as csvf:
        csv_reader = csv.reader(csvf)
        rows = list(csv_reader)

    count = 0
    with open("users.csv", "w") as csvf:
        csv_writer = csv.writer(csvf)
        for row in rows:
            if row[0] == first and row[1] == last:
                count += 1
            else:
                csv_writer.writerow(row)

    return 'Users deleted: {}.'.format(count)
