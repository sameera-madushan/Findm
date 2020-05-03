# Findm - Duplicate Files Finder

Findm is a python script to find duplicate file copies in a given directory. 

Findm search the duplicates by computing a hash for every file while considering several other factors. This script is able to find duplicate images, documents, videos and audio files. However, when it comes to audio files, simillar audio files with different bitrates will not be identified as duplicates from this script, because different bit-rates will produce different checksums.  

#### Findm without duplicate files :point_down:

<p align="center">
  <img src="https://user-images.githubusercontent.com/55880211/79068508-192dac00-7ce5-11ea-8ad6-198c65257706.gif">
</p>

#### Findm with duplicate files :point_down:
<p align="center">
  <img src="https://user-images.githubusercontent.com/55880211/79068513-1b900600-7ce5-11ea-9589-a0d1d69d7d90.gif">
</p>

## Git Installation
```
# clone the repo
$ git clone https://github.com/sameera-madushan/Findm.git

# change the working directory to Findm
$ cd Findm
```

## Usage

```
python findm.py
```

## Support & Contributions
- Please ⭐️ this repository if this project helped you!
- Contributions of any kind welcome!

## License
MIT ©[sameera-madushan](https://github.com/sameera-madushan)

## References
https://stackoverflow.com/a/36113168/13276219

