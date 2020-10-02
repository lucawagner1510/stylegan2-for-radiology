# stylegan2 for radiology
Unofficial implementation of StyleGAN2 for artificial mammograms generation to increase the mammography datasets without using the usual data augmentation methods.

Convolutional Neural Networks can be trained for cancer classification using datasets containing both the original images and those created synthetically using Stylegan2.  

The images were downloaded from https://wiki.cancerimagingarchive.net/display/Public/CBIS-DDSM  and subsequently preprocessed and reduced to 255x256 and 512x512 sizes.  

Stylegan2 training is underway to obtain more control over the stability of convergence. 
The problem of GAN training difficulty is well highlighted in the following article: https://towardsdatascience.com/10-lessons-i-learned-training-generative-adversarial-networks-gans-for-a-year-c9071159628

Train Stylegan2 for radiology:
https://colab.research.google.com/drive/13iOl4zu-YjCaov_NAl_icU479zBh5uaI?usp=sharing

Code and mammograms preprocessed dataset on: 
https://drive.google.com/drive/folders/1ZUYPbVMJECE9U4MSr-ykc6deaj51FF_W?usp=sharing






