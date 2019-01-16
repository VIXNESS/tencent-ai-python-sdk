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
3. 调用
范例:
```python
with open('image.jpg') as image:
  response = aiObj.ocrIDCardOCR(image.read(), 0)
```
## 调用方法

| 方法名称                                                     | 接口名称                   |
| ------------------------------------------------------------ | -------------------------- |
| ``ocrIDCardOCR(image, card_type)``                           | 身份证OCR                  |
| ``ocrDriverLicenseOCR( image, type)``                        | 行驶证/驾驶证OCR           |
| ``ocrGeneralOCR(image)``                                     | 通用OCR                    |
| ``ocrBizLicenseOCR(image)``                                  | 营业执照OCR                |
| ``ocrCreditCardOCR(image)``                                  | 银行卡OCR                  |
| ``ocrHandwritingOCR(image)``                                 | 手写体OCR                  |
| ``ocrPlateOCR(image)``                                       | 车牌OCR                    |
| ``ocrBCOCR(image)``                                          | 名片OCR                    |
| ``faceDetectFace(image, mode)``                              | 人脸分析与检测             |
| ``faceDetectMultiFace(image)``                               | 多人人脸检测               |
| ``faceDetectCrossAgeFace(source_image, target_image)``       | 跨年龄人脸识别             |
| ``faceFaceShape(image, mode)``                               | 五官定位                   |
| ``faceFaceCompare(image_a, image_b)``                        | 人脸对比                   |
| ``faceFaceIdentify(image, group_id, topn)``                  | 人脸搜索                   |
| ``faceNewPerson(group_ids, person_id, image, person_name, tag)`` | 个体创建                   |
| ``faceDelPerson(person_id)``                                 | 个体删除                   |
| ``faceAddFace(person_id, images, tag)``                      | 增加人脸                   |
| `faceDelFace(person_id, face_ids)`                           | 删除人脸                   |
| ``faceSetInfo(person_id, person_name, tag``                  | 设置信息                   |
| `faceGetInfo(person_id)`                                     | 获取信息                   |
| `faceGetGroupIDs()`                                          | 获取组列表                 |
| `faceGetPersonIDs(group_id)`                                 | 获取个体列表               |
| `faceGetfaceIDs(person_id)`                                  | 获取人脸列表               |
| `faceGetfaceInfo(face_id)`                                   | 获取人脸信息               |
| `faceFaceVerify(image, person_id)`                           | 人脸验证                   |
| `ptuImgFilter(filter, image)`                                | 图片滤镜（天天P图）        |
| `visionImgFilter(filter, image, session_id)`                 | 图片滤镜（AI Lab）         |
| `` ptuFaceCosmetic(cosmetic, image)``                        | 人脸美妆                   |
| ``ptuFaceDecoration(decoration, image)``                     | 人脸变装                   |
| `` ptuFaceSticker(sticker, image)``                          | 大头贴                     |
| ``ptuFaceAge(image)``                                        | 颜龄测试                   |
| ``visionImgToText(image, session_id)``                       | 看图说话                   |
| ``imageTag(image)``                                          | 多标签识别                 |
| ``imageFuzzy(image)``                                        | 模糊图片识别               |
| `` imageFood(image)``                                        | 美食图片识别               |
| `` visionScener(format, topk, image)``                       | 场景识别                   |
| `` visionObjectr(format, topk, image)``                      | 物体识别                   |
| ``imageTerrorism(image)``                                    | 暴恐识别                   |
| `` visionPorn(image)``                                       | 图片鉴黄                   |
| ``nlpTextChat(session, question)``                           | 只能闲聊                   |
| ``nlpTextTrans(type, text)``                                 | 文本翻译（AI Lab）         |
| ``nlpTextTranslate(text, source, target)``                   | 文本翻译（翻译君）         |
| `nlpSpeechTranslate(format, seq, end, session_id, speech_chunk, source, target)` | 语音翻译                   |
| `nlpImageTranslate(image, session_id, scene, source, target)` | 图片翻译                   |
| `nlpTextDetect(text, candidate_langs, force)`                | 语种识别                   |
| `nlpWordCom(text)`                                           | 意图成分                   |
| `nlpTextPolar(text)`                                         | 情感分析                   |
| `aaiAsrs(format, rate, seq, len, end, speech_id, speech_chunk)` | 语音识别-echo版            |
| `aaiWxAsrs(format, rate, bits, seq, len, end, speech_id, speech_chunk, cont_res)` | 语音识别-流式版（AI Lab）  |
| `aaiWxAsrs(format, rate, bits, seq, len, end, speech_id, speech_chunk, cont_res)` | 语音识别-流式版(WeChat AI) |
| `aaiWxAsrLong(format, callback_url, speech)`                 | 长语音识别                 |
| `aaiDetectKeyword(format, callback_url, key_words, speech)`  | 关键字检索                 |
| `aaiTTS(speaker, format, volume, speed, text, aht, apc)`     | 语音合成（AI Lab）         |
| `aaiTTA(self, text, model_type, speed)`                      | 语音合成（优图）           |



## 返回值

+ 返回类型为**dictionary**
+ 若有网络请求相关的错误会返回JSON格式的异常(和官方Demo一样)

## :warning:注意事项
+ 所有二进制文件无需base64加密, 传入二进制数据即可(即``file.read()``)
+ ~~需要编码GBK的请求无需GBK转码, 传入即可~~(GBK相关的功能响应都有乱码影响)
+ 有URL与文件二选一的调用方法, 直接传入URL或者文件的二进制数据即可

###  :x: 未实现的功能 

| 官方接口名称            | 调用方法     | 原因         |
| ----------------------- | ------------ | ------------ |
| 音频鉴黄/音频敏感词检测 | aaiEvilAudio | sign invalid |



## :bangbang:缺陷功能

| 官方接口名称        | 调用方法   | 原因                                      |
| ------------------- | ---------- | ----------------------------------------- |
| 图片鉴黄            | visionPorn | 传入URL则会sign invalid, 可使用文件直传输 |
| 基础文本分析-分词   | nlpWordSeg | 响应参数部分乱码                          |
| 基础文本分析-词性   | nlpWordPos | 响应参数部分乱码                          |
| 基础文本分析-反义词 | nlpWordNer | ner word not found                        |
| 基础文本分析-同义词 | nlpWordSyn | syn word not found                        |



## 写在后面的话

> + **音频鉴黄/音频敏感词检测** 这个功能的接口鉴权很奇怪, 都是使用同一套算法,都是传入URL地址,结果其他的功能正常,这个不正常
> + **基础文本分析** 已经成功的将字符GBK编码并且发送的,但是返回的JSON中’text‘字段UTF-8 decode正常,后面部分的不论是使用GBK还是UTF都无法正确的显示

