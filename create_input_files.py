from utils import create_input_files

if __name__ == '__main__':
    # Create input files (along with word map)
    create_input_files(dataset='fashion',
                       karpathy_json_path='/home/ubuntu/filestore/keshav/show-attend-tell/data/dataset_fashion.json',
                       image_folder='/home/ubuntu/filestore/fashion_gen_data/images/',
                       captions_per_image=1,
                       min_word_freq=5,
                       output_folder='/home/ubuntu/filestore/keshav/show-attend-tell/output/fashion/',
                       max_len=30)
