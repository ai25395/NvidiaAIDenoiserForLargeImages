# NvidiaAIDenoiserForLargeImages
By cutting a large image into parts to make NvidiaAIDenoiser(by DeclanRussell,https://declanrussell.com/portfolio/nvidia-ai-denoiser/) work better

-----------------What is this for?-----------------  
When using the NvidiaAIDenoiser(version2.4),I find that there will be a error listed below if you input a very large image(for me it's a 16450*7000 image).  
  
[OptiX]: Unknown error (Details: Function "_rtCommandListExecute" caught exception: Denoiser: getting memory resources failed. input resolution too large, tensor size 6467543040 (max 4294967295)  
input resolution too large, tensor size 6807937024 (max 4294967295)  
  
Obviously,it means the input image is too large for the optix to process at once.  
So,I write a python script which cut the image into small parts,use Denoiser to process them separately and finally make them one image again.  

-----------------How to use it?-----------------  
1.First,ensure you have installed a python and the package 'cv2'  
2.You need to put the 'denoise.py' script into the directory of 'Denoiser_v2.4'(at least for now it's v2.4)  
3.Make a new directory called 'pic' in the 'Denoiser_v2.4' and put the image(for example: apple.png) you want to process into 'pic'  
4.Open cmd or powershell, use 'cd' to go to 'Denoiser_v2.4',then use 'python denoise.py apple.png' to denoise the apple.png.  




