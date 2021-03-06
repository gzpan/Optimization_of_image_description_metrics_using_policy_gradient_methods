#！ encoding: UTF-8

import os
from pycocotools.coco import COCO
from pycocoevalcap.eval import COCOEvalCap

annFile = "../data/train_val_all_reference.json"
resFile = "captions_val2014_results.json"

# create coco object and cocoRes object
coco = COCO(annFile)

# after generating the captions_val2014_results.json file
# we call the coco caption evaluation tools
cocoRes = coco.loadRes(resFile)

# create cocoEval object by taking coco and cocoRes
cocoEval = COCOEvalCap(coco, cocoRes)

# evaluate on a subset of images by setting
# cocoEval.params['image_id'] = cocoRes.getImgIds()
# please remove this line when evaluating the full validation set
cocoEval.params['image_id'] = cocoRes.getImgIds()

# evaluate results
cocoEval.evaluate() 

# print output evaluation scores
for metric, score in cocoEval.eval.items():
    print '%s: %.3f'%(metric, score)