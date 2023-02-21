import pdf
import model
import utils
import ai
import Constants


key = Constants.OPEN_AI_API_KEY
file_name = 'data_file.pdf'

ai.use_key(key)


try:
    out = model.index_file(file_name, fix_text=True, frag_size=200)
    utils.save_dict_to_file(out, 'embeddings.json')
    print("Embeddings created successfully!")
except:
    print('An Error Occured while creating embeddings!')

