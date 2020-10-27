# stylegan2 for radiology


StyleGAN2 implementation for artificial mammograms generation to increase the mammography datasets without using the usual data augmentation methods.

Convolutional Neural Networks can be trained for cancer classification using datasets containing both the original images and those created synthetically using Stylegan2.  

The images were downloaded from https://wiki.cancerimagingarchive.net/display/Public/CBIS-DDSM  and subsequently preprocessed and reduced to 255x256 and 512x512 sizes.  

Stylegan2 training is underway to obtain more control over the stability of convergence. 
The problem of GAN training difficulty is well highlighted in the following article: https://towardsdatascience.com/10-lessons-i-learned-training-generative-adversarial-networks-gans-for-a-year-c9071159628


Code and mammograms preprocessed dataset on: 
https://drive.google.com/drive/folders/1ZUYPbVMJECE9U4MSr-ykc6deaj51FF_W?usp=sharing

I want to increase a small dataset (3200 images) using GANs but initially the network doesn't converge because the too high learning rate and so I reduced it to lr = 0.000001.

However, the dataset is too small: GANs need a lot more images to give good results.
So if you have a small dataset, creating artificial images with GANs doesn't seem like an effective solution, but...

...I found this paper https://github.com/lucidrains/stylegan2-pytorch where the author says:

"However, in the month of May 2020, researchers all across the world independently converged on a simple technique to reduce that number to as low as 1-2k. That simple idea was to differentiably augment all images, generated or real, going into the discriminator during training."

I'll investigate on it using  stylegan2 implementation in Pytorch in Google Colab:  stylegan2_pytorch.ipynb 





