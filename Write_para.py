import datetime
import json


def save_paragraph_to_file(para):
    try:
        current_datetime = datetime.datetime.now()
        date_time = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")
        file_name = f"files_{date_time}.txt"

        with open(file_name, "w") as file:
            file.write(para)

        print(f"Paragraph successfully saved to {file_name}")
        return file_name

    except Exception as e:
        print(f"Error occurred: file not created {e}")


def convert_txt_to_json(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()

        output_file_name = file_name.replace('.txt', '.json')
        with open(output_file_name, 'w') as json_file:
            json.dump({"text_content": content}, json_file, indent=4)

        print(f"Data from '{file_name}' successfully converted and saved to '{output_file_name}' as JSON.")
        return output_file_name  # Return the JSON filename

    except Exception as e:
        print(f"Error occurred while converting .txt to .json: {e}")


def count_paragraphs_words(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()

            paragraphs = content.split('\n\n')
            para_count = len(paragraphs)

            word_count_total = 0
            for paraa, para in enumerate(paragraphs):
                words = para.split()
                word_count = len(words)

                word_count_total += word_count

            output_file_name = file_name.replace('.txt', '.json')
            with open(output_file_name, 'r+') as json_file:
                existing_data = json.load(json_file)
                existing_data["para-count"] = para_count
                existing_data["word-count-total"] = word_count_total
                json_file.seek(0)
                json.dump(existing_data, json_file, indent=4)

            print(f"Results updated and saved to {output_file_name}")
            return output_file_name

    except Exception as e:
        print(f"Error occurred: {e}")
        return None


if __name__ == "__main__":
    user_input = input("Enter a paragraph: ")
    saved_file = save_paragraph_to_file(user_input)

    if saved_file:  # Proceed if the paragraph was successfully saved to a file
        file_input = input("Enter the filename to convert to JSON (including the .txt extension): ")

        json_file = convert_txt_to_json(file_input)
        result_json = count_paragraphs_words(saved_file)

        print(f"Paragraph saved to : {saved_file}")
        print(f"File converted to JSON: {json_file}")
        print(f"Results are : {result_json}")
