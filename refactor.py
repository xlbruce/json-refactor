import json
import logging
import sys
import os

path = os.path.join(os.path.abspath(sys.argv[1]))
logging.basicConfig(filename='app.log', filemode='w', level=logging.DEBUG)

logging.debug('Executing in debug mode')
logging.debug('path: {}'.format(path))

for root, dirs, files in os.walk(path):
    logging.debug('root directory: {}'.format(root))
    for file in files:
        if not file.endswith('.json'):
            logging.info('Ignoring file {}'.format(file))
            continue

        filename = os.path.join(root, file)
        logging.debug('Opening {}'.format(filename))
        with open(filename, 'r') as f:
            obj = json.load(f)
            try:
                real_content = next(iter(obj['content']))
                logging.debug('Parsed successfully')
            except StopIteration:
                logging.info('{} doesn\'t appear to be a valid file'.format(file))
                continue

            for key, value in obj['content'][real_content].items():
                logging.debug('Adding ["{}":"{}"] to "content"'.format(key, value))
                obj['content'][key] = value

            logging.debug('Removing content[{}]'.format(real_content))
            obj['content'].pop(real_content, None)


        with open('target.json', 'w+') as f:
            f.write(json.dumps(obj, indent=4))
            f.flush()
            f.close()
