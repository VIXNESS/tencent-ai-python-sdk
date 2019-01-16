#-*- coding: UTF-8 -*-
from requests import exceptions 
import hashlib
import urllib
import base64
import requests
import json
import time
import os

class AI(object):
    urlPreffix = "https://api.ai.qq.com/fcgi-bin"
    
    def __init__(self, app_id, app_key):
        self.app_id = app_id
        self.app_key = app_key
        self.data = {}
        
    def setBaseInfo(self):
        self.setParams('app_id', self.app_id)
        self.setParams('app_key', self.app_key)
        self.setParams('time_stamp', int(time.time()))
        self.setParams('nonce_str', int(time.time()))
    
    def setParams(self, key, value):
        self.data[key] = value
            
    def sign(self, encode):
        uri_str = ''
        for key in sorted(self.data.keys()):
            if key == 'app_key':
                continue
            uri_str += key + "=" + urllib.parse.quote_plus(str(self.data[key])) + "&"
        sign_str = uri_str + 'app_key=' + self.data['app_key']
        self.setParams('sign', hashlib.md5(sign_str.encode(encode)).hexdigest().upper())
        
    def invoke(self, url, method = 'POST', encode = 'utf-8'):
        self.setBaseInfo()
        self.sign(encode)
        try:
            if method == 'GET':
                response = requests.get(self.urlPreffix + url , params = self.data)
            else:
                response = requests.post(self.urlPreffix + url, data = self.data)
            if encode == 'gbk':
                response.encoding = 'utf-8'
            return response.json()
        except json.JSONDecodeError as e:
            error = {}
            error['ret'] = -1
            error['msg'] = e.msg
            error['httpcode'] = response.status_code
            return error
        except exceptions.RequestException as e:
            error = {}
            error['ret'] = -1
            error['msg'] = e.message
            error['httpcode'] = response.status_code
            return error
        except exceptions.ConnectionError as e:
            error = {}
            error['ret'] = -1
            error['msg'] = e.message
            error['httpcode'] = response.status_code
            return error
        except exceptions.HTTPError as e:
            error = {}
            error['ret'] = -1
            error['msg'] = e.message
            error['httpcode'] = response.status_code
            return error
        except exceptions.Timeout as e:
            error = {}
            error['ret'] = -1
            error['msg'] = e.message
            error['httpcode'] = response.status_code
            return error
        except exceptions.RequestException as e:
            error = {}
            error['ret'] = -1
            error['msg'] = e.message
            error['httpcode'] = response.status_code
            return error
        else:
            error = {}
            error['ret'] = -1
            error['msg'] = -1
            error['httpcode'] = "System Error"
            return error
        return respone.json()
    
    def ocrIDCardOCR(self, image, card_type): 
        self.setParams('image', base64.b64encode(image).decode('utf-8'))
        self.setParams('card_type', card_type)
        return self.invoke('/ocr/ocr_idcardocr')
    
    def ocrDriverLicenseOCR(self, image, type):
        self.setParams('image', base64.b64encode(image).decode('utf-8'))
        self.setParams('type', type)
        return self.invoke('/ocr/ocr_driverlicenseocr')
        
    def ocrGeneralOCR(self, image):
        self.setParams('image', base64.b64encode(image).decode('utf-8'))
        return self.invoke('/ocr/ocr_generalocr')
        
    def ocrBizLicenseOCR(self, image):
        self.setParams('image', base64.b64encode(image).decode('utf-8'))
        return self.invoke('/ocr/ocr_bizlicenseocr')
    
    def ocrCreditCardOCR(self, image):
        self.setParams('image', base64.b64encode(image).decode('utf-8'))
        return self.invoke('/ocr/ocr_creditcardocr')
    
    def ocrHandwritingOCR(self, image):
        if isinstance(image, str):
            self.setParams('image_url', image)
        else:
            self.setParams('image', base64.b64encode(image).decode('utf-8'))
        return self.invoke('/ocr/ocr_handwritingocr')
   
    def ocrPlateOCR(self, image):
        if isinstance(image, str):
            self.setParams('image_url', image)
        else:
            self.setParams('image', base64.b64encode(image).decode('utf-8'))
        return self.invoke('/ocr/ocr_plateocr')

    def ocrBCOCR(self, image):
        self.setParams('image', base64.b64encode(image).decode('utf-8'))
        return self.invoke('/ocr/ocr_bcocr')
    
    def faceDetectFace(self, image, mode):
        self.setParams('image', base64.b64encode(image).decode('utf-8'))
        self.setParams('mode', mode)
        return self.invoke('/face/face_detectface')
        
    def faceDetectMultiFace(self, image):
        self.setParams('image', base64.b64encode(image).decode('utf-8'))
        return self.invoke('/face/face_detectmultiface')
    
    def faceDetectCrossAgeFace(self, source_image, target_image):
        self.setParams('source_image', base64.b64encode(source_image).decode('utf-8'))
        self.setParams('target_image', base64.b64encode(target_image).decode('utf-8'))
        return self.invoke('/face/face_detectcrossageface')
    
    def faceFaceShape(self, image, mode):
        self.setParams('image', base64.b64encode(image).decode('utf-8'))
        self.setParams('mode', mode)
        return self.invoke('/face/face_faceshape')
        
    def faceFaceCompare(self, image_a, image_b):
        self.setParams('image_a', base64.b64encode(image_a).decode('utf-8'))
        self.setParams('image_b', base64.b64encode(image_b).decode('utf-8'))
        return self.invoke('/face/face_facecompare')
    
    def faceFaceIdentify(self, image, group_id, topn):
        self.setParams('image', base64.b64encode(image).decode('utf-8'))
        self.setParams('group_id', group_id)
        self.setParams('topn', topn)
        return self.invoke('/face/face_faceidentify')
    
    def faceNewPerson(self, group_ids, person_id, image, person_name, tag):
        self.setParams('image', base64.b64encode(image).decode('utf-8'))
        self.setParams('group_ids', group_ids)
        self.setParams('person_id',person_id)
        self.setParams('person_name',person_name)
        if tag != '':
            self.setParams('tag', tag)
        return self.invoke('/face/face_newperson')
        
    def faceDelPerson(self, person_id):
        self.setParams('person_id',person_id)
        return self.invoke('/face/face_delperson')
        
    def faceAddFace(self, person_id, images, tag):
        self.setParams('person_id',person_id)
        self.setParams('image', base64.b64encode(image).decode('utf-8'))
        self.setParams('tag', tag)
        return self.invoke('/face/face_addface')
    
    def faceDelFace(self, person_id, face_ids):
        self.setParams('person_id',person_id)
        self.setParams('face_ids',face_ids)
        return self.invoke('/face/face_delface')
        
    def faceSetInfo(self, person_id, person_name, tag):
        self.setParams('person_id',person_id)
        if person_name != '':
            self.setParams('person_id', person_id)
        if tag != '':
            self.setParams('tag', tag)
        return self.invoke('/face/face_setinfo')
        
    def faceGetInfo(self, person_id):
        self.setParams('person_id',person_id)
        return self.invoke('/face/face_getinfo')
        
        
    def faceGetGroupIDs(self):
        return self.invoke('/face/face_getgroupids')
        
    def faceGetPersonIDs(self, group_id):
        self.setParams('group_id', group_id)
        return self.invoke('/face/face_getpersonids')
    
    def faceGetfaceIDs(self, person_id):
        self.setParams('person_id', person_id)
        return self.invoke('/face/face_getfaceids')
        
    def faceGetfaceInfo(self, face_id):
        self.setParams('face_id', face_id)
        return self.invoke('/face/face_getfaceinfo')
    
    def faceFaceVerify(self, image, person_id):
        self.setParams('image', base64.b64encode(image).decode('utf-8'))
        self.setParams('person_id',person_id)
        return self.invoke('/face/face_faceverify')
        
    def ptuImgFilter(self, filter, image):
        self.setParams('filter', filter)
        self.setParams('image', base64.b64encode(image).decode('utf-8'))
        return self.invoke('/ptu/ptu_imgfilter')
        
    def ptuFaceCosmetic(self, cosmetic, image):
        self.setParams('cosmetic', cosmetic)
        self.setParams('image', base64.b64encode(image).decode('utf-8'))
        return self.invoke('/ptu/ptu_facecosmetic')
    
    def ptuFaceDecoration(self, decoration, image):
        self.setParams('decoration', decoration)
        self.setParams('image', base64.b64encode(image).decode('utf-8'))
        return self.invoke('/ptu/ptu_facedecoration')
        
    def ptuFaceSticker(self, sticker, image):
        self.setParams('sticker', sticker)
        self.setParams('image', base64.b64encode(image).decode('utf-8'))
        return self.invoke('/ptu/ptu_facesticker')
        
    def ptuFaceAge(self, image):
        self.setParams('image', base64.b64encode(image).decode('utf-8'))
        return self.invoke('/ptu/ptu_faceage')
    
    def visionImgToText(self, image, session_id): 
        self.setParams('image', base64.b64encode(image).decode('utf-8'))
        self.setParams('session_id', session_id)
        return self.invoke('/vision/vision_imgtotext')
        
    def imageTag(self, image):
        self.setParams('image', base64.b64encode(image).decode('utf-8'))
        return self.invoke('/image/image_tag')
    
    def imageFuzzy(self, image):
        self.setParams('image', base64.b64encode(image).decode('utf-8'))
        return self.invoke('/image/image_fuzzy')
    
    def imageFood(self, image):
        self.setParams('image', base64.b64encode(image).decode('utf-8'))
        return self.invoke('/image/image_food')
        
    def visionScener(self, format, topk, image):
        self.setParams('format', format)
        self.setParams('topk', topk)
        self.setParams('image', base64.b64encode(image).decode('utf-8'))
        return self.invoke('/vision/vision_scener')
        
    def visionObjectr(self, format, topk, image):
        self.setParams('format', format)
        self.setParams('topk', topk)
        self.setParams('image', base64.b64encode(image).decode('utf-8'))
        return self.invoke('/vision/vision_objectr')
    
    def imageTerrorism(self, image): #url mode failure
        if isinstance(image, str):
            self.setParams('image_url', image)
        else:
            self.setParams('image', base64.b64encode(image).decode('utf-8'))
        return self.invoke('/image/image_terrorism', 'POST')
    
    def visionPorn(self, image): # url mode failure
        if isinstance(image, str):
            self.setParams('image_url', image)
        else: 
            self.setParams('image', base64.b64encode(image).decode('utf-8'))
        return self.invoke('/vision/vision_porn', 'POST')
        
#    def aaiEvilAudio(self, speech_id, speech_url, porn_detect, keyword_detect): #sign invalid
#        self.setParams('speech_id', speech_id)
#        self.setParams('speech_url', speech_url)
#        self.setParams('porn_detect', porn_detect)
#        self.setParams('keyword_detect', keyword_detect)
#        return self.invoke('/aai/aai_evilaudio', 'GET')
    
    def nlpTextChat(self, session, question):
        self.setParams('session', session)
        self.setParams('question', question)
        return self.invoke('/nlp/nlp_textchat')
        
    def nlpTextTrans(self, type, text):
        self.setParams('type', type)
        self.setParams('text', text)
        return self.invoke('/nlp/nlp_texttrans')
        
    def nlpTextTranslate(self, text, source, target): 
        self.setParams('text', text)
        self.setParams('source', source)
        self.setParams('target', target)
        return self.invoke('/nlp/nlp_texttranslate')
        
    def nlpSpeechTranslate(self ,format, seq, end, session_id, speech_chunk, source, target):
        self.setParams('format',format)
        self.setParams('seq', seq)
        self.setParams('end', end)
        self.setParams('session_id', session_id)
        self.setParams('speech_chunk', base64.b64encode(speech_chunk).decode('utf-8'))
        self.setParams('source', source)
        self.setParams('target', target)
        return self.invoke('/nlp/nlp_speechtranslate')
        
    def nlpImageTranslate(self, image, session_id, scene, source, target):
        self.setParams('image', base64.b64encode(image).decode('utf-8'))
        self.setParams('session_id', session_id)
        self.setParams('scene', scene)
        self.setParams('source', source)
        self.setParams('target', target)
        return self.invoke('/nlp/nlp_imagetranslate')
    
    def nlpTextDetect(self, text, candidate_langs, force):
        self.setParams('text', text)
        self.setParams('candidate_langs', candidate_langs)
        self.setParams('force', force)
        return self.invoke('/nlp/nlp_textdetect')
        
    def nlpWordSeg(self, text):#GBK encoding error
        self.setParams('text', text)
        return self.invoke('/nlp/nlp_wordseg', encode = 'gbk')    
    def nlpWordPos(self, text):#GBK encoding error
        self.setParams('text', text)
        return self.invoke('/nlp/nlp_wordpos', encode = 'gbk')
        
    def nlpWordNer(self, text):#GBK encoding error
        self.setParams('text', text)
        return self.invoke('/nlp/nlp_wordner', encode = 'gbk')
        
    def nlpWordSyn(self, text):#GBK encoding error
        self.setParams('text', text)
        return self.invoke('/nlp/nlp_wordsyn', encode = 'gbk')
    
    def nlpWordCom(self, text):
        self.setParams('text', text)
        return self.invoke('/nlp/nlp_wordcom', encode = 'gbk')
    
    def nlpTextPolar(self, text):
        self.setParams('text', text)
        return self.invoke('/nlp/nlp_textpolar')
    
    def aaiAsr(self, format, speech, rate = 16000):
        self.setParams('format', format)
        self.setParams('speech', base64.b64encode(speech).decode('utf-8'))
        self.setParams('rate', rate)
        return self.invoke('/aai/aai_asr')
        
    def aaiAsrs(self, format, rate, seq, len, end, speech_id, speech_chunk):
        self.setParams('format', format)
        self.setParams('rate', rate)
        self.setParams('seq', seq)
        self.setParams('len', len)
        self.setParams('end', end)
        self.setParams('speech_id', speech_id)
        self.setParams('speech_chunk', base64.b64encode(speech_chunk).decode('utf-8'))
        return self.invoke('/aai/aai_asrs')
        
    def aaiWxAsrs(self, format, rate, bits, seq, len, end, speech_id, speech_chunk, cont_res):
        self.setParams('format', format)
        self.setParams('rate', rate)
        self.setParams('bits', bits)
        self.setParams('seq', seq)
        self.setParams('len', len)
        self.setParams('end', end)
        self.setParams('speech_id', speech_id)
        self.setParams('speech_chunk', base64.b64encode(speech_chunk).decode('utf-8'))
        self.setParams('cont_res', cont_res)
        return self.invoke('/aai/aai_wxasrs')
        
    def aaiWxAsrLong(self, format, callback_url, speech):
        self.setParams('format' ,format)
        self.setParams('callback_url', callback_url)
        if isinstance(speech, str):
            self.setParams('speech_url', speech_url)
        else:
            self.setParams('speech', base64.b64encode(speech).decode('utf-8'))
        return self.invoke('/aai/aai_wxasrlong')
        
    def aaiDetectKeyword(self, format, callback_url, key_words, speech):
        self.setParams('format' ,format)
        self.setParams('callback_url', callback_url)
        self.setParams('key_words', key_words)
        if isinstance(speech, str):
            self.setParams('speech_url', speech)
        else:
            self.setParams('speech', base64.b64encode(speech).decode('utf-8'))
        return self.invoke('/aai/aai_detectkeyword')
    
    def aaiTTS(self, speaker, format, volume, speed, text, aht, apc):
        self.setParams('speaker', speaker)
        self.setParams('format', format)
        self.setParams('volume', volume)
        self.setParams('speed', speed)
        self.setParams('text', text)
        self.setParams('aht', aht)
        self.setParams('apc', apc)
        return self.invoke('/aai/aai_tts', method = 'GET')
        
    def aaiTTA(self, text, model_type, speed):
        self.setParams('text', text)
        self.setParams('model_type', model_type)
        self.setParams('speed', speed)
        return self.invoke('/aai/aai_tta', method = 'GET')
