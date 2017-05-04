# ML_Capstone ( Human Action Recognition and Video Classification using SVM and Deep-CNN )

## code instructions
Please install requirement packages from requirements.txt file.
Please download data files from this site http://crcv.ucf.edu/data/UCF101/UCF101.rar {br/}
`SVM`
1. To create train and test data for SVM run the following commands {br/}
python split_data.py train
python split_data.py test
This will create train and test folder with relevant video frames.
2. To train and test the above created data run the following command__
python walk.py

`CNN`
1. To create train and test data for CNN run the following commands__
python split_data_cnn.py train
python split_data_cnn.py test
This will create train and test folder with relevant video frames.
2. To convert our dataset according to Cifar10 format follow following steps
git clone https://github.com/gskielian/PNG-2-CIFAR10
run ./resize-script.sh to resize image frames to 32*32 rgb pixels
now run, python convert-images-to-cifar-format.py 
this will create batch file for train and test.
Copy and paste these files to /tmp/cifar10-data/ folder
3. Next train cifar10 model on our above created dataset
python cifar10/cifar10_train.py 

4. To test from trained cifar10 model try
python cifar10_eval.py
