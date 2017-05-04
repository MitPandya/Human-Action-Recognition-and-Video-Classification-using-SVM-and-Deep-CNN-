# ML_Capstone ( Human Action Recognition and Video Classification using SVM and Deep-CNN )

## code instructions
Please install requirement packages from requirements.txt file.
Please download data files from this site http://crcv.ucf.edu/data/UCF101/UCF101.rar
`SVM`
1. To create train and test data for SVM run the following commands
python split_data.py train
python split_data.py test
This will create train and test folder with relevant video frames.
2. To train and test the above created data run the following command
python walk.py
