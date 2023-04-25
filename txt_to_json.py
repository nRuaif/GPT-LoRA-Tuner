import json

def split_text_to_jsonl(txt_file):
  """Splits text into a JSONL file, with 2 attributes: prompt and input. Input is empty while prompt is a paragraph from the txt file.

  Args:
    txt_file: The path to the txt file to split.

  Returns:
    A JSONL file containing the split text.
  """

  with open("text.txt", 'r', encoding = "UTF-8") as f:
    text = f.read()

  paragraphs = text.split('\n\n')

  with open('output.jsonl', 'w') as f:
    for paragraph in paragraphs:
      prompt = paragraph.strip()
      input = ''

      data = {
        'prompt': prompt,
        'input': input,
      }

      json.dump(data, f, indent=2)
      f.write('\n')

if __name__ == '__main__':
  txt_file = 'input.txt'

  split_text_to_jsonl(txt_file)
