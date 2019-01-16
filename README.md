# Tencent AI Python3 SDK
>  腾讯AI 非官方的Python3 SDK

## 用法
1. 装载文件
```python
import sys
sys.path.append('文件所在目录') 
import tencentai
```
2. 初始化
```python
aiObj = tencentai.AI('你的AppID', '你的AppKey')
```
3. 调用范例:
```python
with open('image.jpg') as image:
  response = aiObj.ocrIDCardOCR(image.read(), 0)
```
## 调用方法

| 官方接口名称 | 方法名称                                                     | 请求连接                      |
| ------------ | ------------------------------------------------------------ | ----------------------------- |
|              | ``ocrIDCardOCR(image, card_type)``                           | /ocr/ocr_idcardocr            |
|              | ``ocrDriverLicenseOCR( image, type)``                        | /ocr/ocr_driverlicenseocr     |
|              | ``ocrGeneralOCR(image)``                                     | /ocr/ocr_generalocr           |
|              | ``ocrBizLicenseOCR(image)``                                  | /ocr/ocr_bizlicenseocr        |
|              | ``ocrCreditCardOCR(image)``                                  | /ocr/ocr_creditcardocr        |
|              | ``ocrHandwritingOCR(image)``                                 | /ocr/ocr_handwritingocr       |
|              | ``ocrPlateOCR(image)``                                       | /ocr/ocr_plateocr             |
|              | ``ocrBCOCR(image)``                                          | /ocr/ocr_bcocr                |
|              | ``faceDetectFace(image, mode)``                              | /face/face_detectface         |
|              | ``faceDetectMultiFace(image)``                               | /face/face_detectmultiface    |
|              | ``faceDetectCrossAgeFace(source_image, target_image)``       | /face/face_detectcrossageface |
|              | ``faceFaceShape(image, mode)``                               | /face/face_faceshape          |
|              | ``faceFaceCompare(image_a, image_b)``                        | /face/face_facecompare'       |
|              | ``faceFaceIdentify(image, group_id, topn)``                  | /face/face_faceidentify       |
|              | ``faceNewPerson(group_ids, person_id, image, person_name, tag)`` | /face/face_newperson          |
|              | ``faceDelPerson(person_id)``                                 | /face/face_delperson          |
|              | ``faceAddFace(person_id, images, tag)``                      | /face/face_addface            |
|              | `faceDelFace(person_id, face_ids)`                           | /face/face_delface            |
|              | ``faceSetInfo(person_id, person_name, tag``                  | /face/face_setinfo            |
|              | `faceGetInfo(person_id)`                                     | /face/face_getinfo            |
|              | `faceGetGroupIDs()`                                          | /face/face_getgroupids        |
|              | `faceGetPersonIDs(group_id)`                                 | /face/face_getpersonids       |
|              | `faceGetfaceIDs(person_id`                                   | /face/face_getfaceids         |
|              | `faceGetfaceInfo(face_id)`                                   | /face/face_getfaceinfo        |
|              | `faceFaceVerify(image, person_id)`                           | /face/face_faceverify         |
|              | ``ptuImgFilter(filter, image)``                              | /ptu/ptu_imgfilter            |
|              | `` ptuFaceCosmetic(cosmetic, image)``                        | /ptu/ptu_facecosmetic         |
|              | ``ptuFaceDecoration(decoration, image)``                     | /ptu/ptu_facedecoration       |
|              | `` ptuFaceSticker(sticker, image)``                          | /ptu/ptu_facesticker          |
|              | ``ptuFaceAge(image)``                                        | /ptu/ptu_faceage              |
|              | ``visionImgToText(image, session_id)``                       | /vision/vision_imgtotext      |
|              | ``imageTag(image)``                                          | /image/image_tag              |
|              | ``imageFuzzy(image)``                                        | /image/image_fuzzy            |
|              | `` imageFood(image)``                                        | /image/image_food             |
|              | `` visionScener(format, topk, image)``                       | /vision/vision_scener         |
|              | `` visionObjectr(format, topk, image)``                      | /vision/vision_objectr        |
|              | ``imageTerrorism(image)``                                    | /image/image_terrorism        |
|              | `` visionPorn(image)``                                       | /vision/vision_porn           |
|              | ``nlpTextChat(session, question)``                           | /nlp/nlp_textchat             |
|              | ``nlpTextTrans(type, text)``                                 | /nlp/nlp_texttrans            |
|              | ``nlpTextTranslate(text, source, target)``                   | /nlp/nlp_texttranslate        |
|              | `nlpSpeechTranslate(format, seq, end, session_id, speech_chunk, source, target)` | /nlp/nlp_speechtranslate      |
|              | `nlpImageTranslate(image, session_id, scene, source, target)` | /nlp/nlp_imagetranslate       |
|              | `nlpTextDetect(text, candidate_langs, force)`                | /nlp/nlp_textdetect           |
|              | `nlpWordCom(text)`                                           | /nlp/nlp_wordcom              |
|              | `nlpTextPolar(text)`                                         | /nlp/nlp_textpolar            |
|              | `aaiAsrs(format, rate, seq, len, end, speech_id, speech_chunk)` | /aai/aai_asrs                 |
|              | `aaiWxAsrs(format, rate, bits, seq, len, end, speech_id, speech_chunk, cont_res)` | /aai/aai_wxasrs               |
|              | `aaiWxAsrLong(self, format, callback_url, speech)`           | /aai/aai_wxasrlong            |
|              | `aaiDetectKeyword(format, callback_url, key_words, speech)`  | /aai/aai_detectkeyword        |
|              | `aaiTTS(self, speaker, format, volume, speed, text, aht, apc)` | /aai/aai_tts                  |
|              | `aaiTTA(self, text, model_type, speed)`                      | /aai/aai_tta                  |



## 返回值

+ 返回类型为**dictionary**
+ 若有网络请求相关的错误会返回JSON格式的异常(和官方Demo一样)

## :warning:注意事项
+ 所有二进制文件无需base64加密, 传入二进制数据即可(即``file.read()``)
+ ~~需要编码GBK的请求无需GBK转码, 传入即可~~
+ 有URL与文件二选一的调用方法, 直接传入URL或者文件的二进制数据即可

###  :x: 无法使用的功能 

| 官方接口名称            | 调用方法     | 原因                                      |
| ----------------------- | ------------ | ----------------------------------------- |
| 音频鉴黄/音频敏感词检测 | aaiEvilAudio | sign invalid                              |
| 图片鉴黄                | visionPorn   | 传入URL则会sign invalid, 可使用文件直传输 |
| 基础文本分析-分词       | nlpWordSeg   | 响应参数部分乱码                          |
| 基础文本分析-词性       | nlpWordPos   | 响应参数部分乱码                          |
| 基础文本分析-反义词     | nlpWordNer   | ner word not found                        |
| 基础文本分析-同义词     | nlpWordSyn   | syn word not found                        |




