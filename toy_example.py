# Import the relevant packages
import nibabel as nib
# This is the nibabel package to load in the NIFTI format 
import matplotlib.pyplot as plt
# This is the usual suspect to import plotting routines

# This next chunk of load loads in the nifti file:
epi_img = nib.load('someones_anatomy.nii.gz')
epi_img_data = epi_img.get_data()
epi_img_data.shape


# This little function then is a way to display the data once you have generated the sliced images:
def show_slices(slices):
   """ Function to display row of image slices """
   fig, axes = plt.subplots(1, len(slices))
   for i, slice in enumerate(slices):
       axes[i].imshow(slice.T, cmap="gray", origin="lower")


# Here where are choosing three slices, as the image is a 3D recontrsuction of someone's brain we have to think about this
# in 3D co-ordinates.

# This first slice is showing images sliced in the "saggital" orientation where the slices show someone's brain where left of the image is the most Anterior position in the brain (close to the eyes) and the right is the Posterior position in the brain (close to the back of the head)
slice_0 = epi_img_data[26, :, :] 
# The second slice is showing images sliced in the "coronal" orientation where the slices show someone's brain where the left and right of the image show the left and right of someone's brain.
slice_1 = epi_img_data[:, 30, :]
# The third slice is showing images sliced in the "axial" orientation where the slices show someone's brain where the top is the Anterior part of the brain, and the bottom is the Posterior part of someone's brain.
slice_2 = epi_img_data[:, :, 16]

# Here now we display all three slices
show_slices([slice_0, slice_1, slice_2])
plt.suptitle("Center slices for EPI image")  
plt.show()