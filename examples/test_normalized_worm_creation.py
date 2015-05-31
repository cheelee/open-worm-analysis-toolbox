# -*- coding: utf-8 -*-
"""
Show how to go from a basic worm to a NormalizedWorm

i.e. NormalizedWorm.from_basicWorm_factory

We then load a pre-calculated NormalizedWorm and verify that they are the same:

i.e. nw == nw_calculated

"""

import sys, os

sys.path.append('..')

from movement_validation import user_config, config, VideoInfo
from movement_validation import WormFeatures, BasicWorm
from movement_validation import NormalizedWorm
from movement_validation import FeatureProcessingOptions


def main():
    # Load from file a normalized worm, as calculated by Schafer Lab code
    base_path = os.path.abspath(user_config.EXAMPLE_DATA_PATH)
    schafer_nw_file_path = os.path.join(base_path, 
                                     "example_video_norm_worm.mat")
    nw = NormalizedWorm.from_schafer_file_factory(schafer_nw_file_path)

    # Load from file some non-normalized contour data, from a file we know
    # to have been generated by the same Schafer code that created the above
    # normalized worm.  This file was generated earlier in the code though,
    # and contains more "primitive", non-normalized contour and skeleton data
    schafer_bw_file_path = os.path.join(base_path, 
                                    "example_contour_and_skeleton_info.mat")  
    bw = BasicWorm.from_schafer_file_factory(schafer_bw_file_path)

    # Compare our generated normalized worm `nw2` with the pre-loaded 
    # Schafer Lab normalized worm, `nw`.  Validate they are the same.
    nw_calculated = NormalizedWorm.from_BasicWorm_factory(bw)
    nw == nw_calculated

    # The frame rate is somewhere in the video info. Ideally this would 
    # all come from the video parser eventually
    fpo = FeatureProcessingOptions(config.FPS)
    video_info = VideoInfo('Example Video File', config.FPS)

    # Generate the OpenWorm movement validation repo version of the features
    fpo.disable_feature_sections(['morphology']) 
    wf = WormFeatures(nw, video_info, fpo)
    
    # Display how long it took to generate each of the features
    wf.timer.summarize()


if __name__ == '__main__':
    main()
