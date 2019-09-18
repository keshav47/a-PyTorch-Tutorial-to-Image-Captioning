from utils import create_input_files

if __name__ == '__main__':
    # Create input files (along with word map)
    create_input_files(dataset='flickr8k',
                       karpathy_json_path='/home/ubuntu/filestore/ms-coco/show-attend-tell/dataset_flickr8k.json',
                       image_folder='/home/ubuntu/filestore/flickr8k/Flickr8k/Flicker8k_Dataset/',
                       captions_per_image=5,
                       min_word_freq=5,
                       output_folder='/home/ubuntu/filestore/keshav/show-attend-tell/output/flickr8k/',
                       max_len=50)
