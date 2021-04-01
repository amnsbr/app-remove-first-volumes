[![Abcdspec-compliant](https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg)](https://github.com/brain-life/abcd-spec)
[![Run on Brainlife.io](https://img.shields.io/badge/Brainlife-bl.app.444-blue.svg)](https://doi.org/10.25663/bl.app.444)

# app-remove-first-volumes
An app to remove the first N volumes of a 4D fMRI image.

This app uses nilearn to remove the first N volumes of a 4D fMRI image, which is a common practice in fMRI preprocessing. The input is a fMRI image (.nii.gz) and the number of volumes to be removed, and the output is another fMRI image (.nii.gz) with the first volumes removed. Notice that this app (for now) should only be used with rs-fMRI images and be run before fmriprep, as it will disrupt the correspondence of regressors timeseries and events with the 4D image.

### Authors
- [Amin Saberi](amnsbr@gmail.com)

#### Copyright (c) 2020 brainlife.io The University of Texas at Austin and Indiana University

### Funding Acknowledgement
brainlife.io is publicly funded and for the sustainability of the project it is helpful to Acknowledge the use of the platform. We kindly ask that you acknowledge the funding below in your code and publications. Copy and past the following lines into your repository when using this code.

[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-1636893](https://img.shields.io/badge/NSF_BCS-1636893-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-ACI-1916518](https://img.shields.io/badge/NSF_ACI-1916518-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1916518)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://grantome.com/grant/NIH/R01-EB029272-01)

### Citations
We ask that you the following articles when publishing papers that used data, code or other resources created by the brainlife.io community.

1. Avesani, P., McPherson, B., Hayashi, S. et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. Sci Data 6, 69 (2019). [https://doi.org/10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)


## Running the App 

### On Brainlife.io

You can submit this App online at ??? via the "Execute" tab.

### Running Locally (on your machine)

1. git clone this repo.
2. Inside the cloned directory, create `config.json` with something like the following content with paths to your input files.

```json
{
    "fmri": "test_bold.nii.gz",
    "n_vols": "5"
}
```

3. Launch the App by executing `main`

```bash
./main
```

## Output

Output file (a 4D .nii.gz file with the first volumes removed) will be generated inside the current working directory (pwd), inside a specifc directory called:

```
out_dir
```

### Dependencies

This App only requires nilearn to run. 
