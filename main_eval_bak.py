#
# For licensing see accompanying LICENSE file.
# Copyright (C) 2023 Apple Inc. All Rights Reserved.
#

from engine.eval_detection import main_detection_evaluation
from typing import List, Optional

'''

# Exectuion:
python main_eval_bak.py --common.config-file config/detection/ssd_coco/moconv2_eval.yaml
python main_eval_bak.py --common.config-file config/detection/ssd_coco/moconv2.yaml

'''

def main_worker_detection(args: Optional[List[str]] = None, **kwargs):
    main_detection_evaluation(args=args, **kwargs)


if __name__ == "__main__":
    main_worker_detection()
