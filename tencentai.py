#-*- coding: UTF-8 -*-
from requests import exceptions 
import hashlib
import urllib
import base64
import requests
import json
import time
import os

class ai(object):
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
            
    def sign(self):
        uri_str = ''
        for key in sorted(self.data.keys()):
            if key == 'app_key':
                continue
            uri_str += key + "=" + urllib.parse.quote_plus(str(self.data[key])) + "&"
        sign_str = uri_str + 'app_key=' + self.data['app_key']
        self.setParams('sign', hashlib.md5(sign_str.encode('utf-8')).hexdigest().upper())
        
    def invoke(self, url, method):
        self.setBaseInfo()
        self.sign()
        try:
            if method == 'GET':
                response = requests.get(self.urlPreffix + url , params = self.data)# data or params?
            else:
                response = requests.post(self.urlPreffix + url, data = self.data)
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
        return self.invoke('/ocr/ocr_idcardocr', 'POST')
    
    def ocrDriverLicenseOCR(self, image, type):
        self.setParams('image', base64.b64encode(image).decode('utf-8'))
        self.setParams('type', type)
        return self.invoke('/ocr/ocr_driverlicenseocr','POST')
        
    def ocrGeneralOCR(self, image):
        self.setParams('image', base64.b64encode(image).decode('utf-8'))
        return self.invoke('/ocr/ocr_generalocr','POST')
        
    def ocrBizLicenseOCR(self, image):
        self.setParams('image', base64.b64encode(image).decode('utf-8'))
        return self.invoke('/ocr/ocr_bizlicenseocr','POST')
    
    def ocrCreditCardOCR(self, image):
        self.setParams('image', base64.b64encode(image).decode('utf-8'))
        return self.invoke('/ocr/ocr_creditcardocr','POST')
    
    def ocrHandwritingOCR(self, image, isURL):
        if isURL:
            self.setParams('image_url', image)
        else:
            self.setParams('image', base64.b64encode(image).decode('utf-8'))
        return self.invoke('/ocr/ocr_handwritingocr','POST')
   
    def ocrPlateOCR(self, image, isURL):
        if isURL:
            self.setParams('image_url', image)
        else:
            self.setParams('image', base64.b64encode(image).decode('utf-8'))
        return self.invoke('/ocr/ocr_plateocr','POST')

    def ocrBCOCR(self, image):
        self.setParams('image', base64.b64encode(image).decode('utf-8'))
        return self.invoke('/ocr/ocr_bcocr','POST')
    
    def faceDetectFace(self, image, mode):
        self.setParams('image', base64.b64encode(image).decode('utf-8'))
        self.setParams('mode', mode)
        return self.invoke('/face/face_detectface', 'POST')
        
    def faceDetectMultiFace(self, image):
        self.setParams('image', base64.b64encode(image).decode('utf-8'))
        return self.invoke('/face/face_detectmultiface', 'POST')
    
    def faceDetectCrossAgeFace(self, source_image, target_image):
        self.setParams('source_image', base64.b64encode(source_image).decode('utf-8'))
        self.setParams('target_image', base64.b64encode(target_image).decode('utf-8'))
        return self.invoke('/face/face_detectcrossageface', 'POST')
    
    def faceFaceShape(self, image, mode):
        self.setParams('image', base64.b64encode(image).decode('utf-8'))
        self.setParams('mode', mode)
        return self.invoke('/face/face_faceshape', 'POST')
        
    def faceFaceCompare(self, image_a, image_b):
        self.setParams('image_a', base64.b64encode(image_a).decode('utf-8'))
        self.setParams('image_b', base64.b64encode(image_b).decode('utf-8'))
        return self.invoke('/face/face_facecompare', 'POST')
    
    def faceFaceIdentify(self, image, group_id, topn):
        self.setParams('image', base64.b64encode(image).decode('utf-8'))
        self.setParams('group_id', group_id)
        self.setParams('topn', topn)
        return self.invoke('/face/face_faceidentify', 'POST')
    
    def faceNewPerson(self, group_ids, person_id, image, person_name, tag):
        self.setParams('image', base64.b64encode(image).decode('utf-8'))
        self.setParams('group_ids', group_ids)
        self.setParams('person_id',person_id)
        self.setParams('person_name',person_name)
        if tag != '':
            self.setParams('tag', tag)
        return self.invoke('/face/face_newperson', 'POST')
        
    def faceDelPerson(self, person_id):
        self.setParams('person_id',person_id)
        return self.invoke('/face/face_delperson', 'POST')
        
    def faceAddFace(self, person_id, images, tag):
        self.setParams('person_id',person_id)
        self.setParams('image', base64.b64encode(image).decode('utf-8'))
        self.setParams('tag', tag)
        return self.invoke('/face/face_addface', 'POST')
    
    def faceDelFace(self, person_id, face_ids):
        self.setParams('person_id',person_id)
        self.setParams('face_ids',face_ids)
        return self.invoke('/face/face_delface', 'POST')
        
    def faceSetInfo(self, person_id, person_name, tag):
        self.setParams('person_id',person_id)
        if person_name != '':
            self.setParams('person_id', person_id)
        if tag != '':
            self.setParams('tag', tag)
        return self.invoke('/face/face_setinfo', 'POST')
        
    def faceGetInfo(self, person_id):
        self.setParams('person_id',person_id)
        return self.invoke('/face/face_getinfo', 'POST')
        
        
    def faceGetGroupIDs(self):
        return self.invoke('/face/face_getgroupids', 'POST')
        
    def faceGetPersonIDs(self, group_id):
        self.setParams('group_id', group_id)
        return self.invoke('/face/face_getpersonids', 'POST')
    
    def faceGetfaceIDs(self, person_id):
        self.setParams('person_id', person_id)
        return self.invoke('/face/face_getfaceids', 'POST')
        
    def faceGetfaceInfo(self, face_id):
        self.setParams('face_id', face_id)
        return self.invoke('/face/face_getfaceinfo', 'POST')
    
    def faceFaceVerify(self, image, person_id):
        self.setParams('image', base64.b64encode(image).decode('utf-8'))
        self.setParams('person_id',person_id)
        return self.invoke('/face/face_faceverify', 'POST')
        
    def ptuImgFilter(self, filter, image):
        self.setParams('filter', filter)
        self.setParams('image', base64.b64encode(image).decode('utf-8'))
        return self.invoke('/ptu/ptu_imgfilter', 'POST')
        
    def ptuFaceCosmetic(self, cosmetic, image):
        self.setParams('cosmetic', cosmetic)
        self.setParams('image', base64.b64encode(image).decode('utf-8'))
        return self.invoke('/ptu/ptu_facecosmetic', 'POST')
    
    def ptuFaceDecoration(self, decoration, image):
        self.setParams('decoration', decoration)
        self.setParams('image', base64.b64encode(image).decode('utf-8'))
        return self.invoke('/ptu/ptu_facedecoration', 'POST')
        
    def ptuFaceSticker(self, sticker, image):
        self.setParams('sticker', sticker)
        self.setParams('image', base64.b64encode(image).decode('utf-8'))
        return self.invoke('/ptu/ptu_facesticker', 'POST')
        
    def ptuFaceAge(self, image):
        self.setParams('image', base64.b64encode(image).decode('utf-8'))
        return self.invoke('/ptu/ptu_faceage', 'POST')
    
    def visionImgToText(self, image, session_id): 
        self.setParams('image', base64.b64encode(image).decode('utf-8'))
        self.setParams('session_id', session_id)
        return self.invoke('/vision/vision_imgtotext', 'POST')
        
    def imageTag(self, image):
        self.setParams('image', base64.b64encode(image).decode('utf-8'))
        return self.invoke('/image/image_tag', 'POST')
    
    def imageFuzzy(self, image):
        self.setParams('image', base64.b64encode(image).decode('utf-8'))
        return self.invoke('/image/image_fuzzy', 'POST')
    
    def imageFood(self, image):
        self.setParams('image', base64.b64encode(image).decode('utf-8'))
        return self.invoke('/image/image_food', 'POST')
        
    def visionScener(self, format, topk, image):
        self.setParams('format', format)
        self.setParams('topk', topk)
        self.setParams('image', base64.b64encode(image).decode('utf-8'))
        return self.invoke('/vision/vision_scener', 'POST')
        
    def visionObjectr(self, format, topk, image):
        self.setParams('format', format)
        self.setParams('topk', topk)
        self.setParams('image', base64.b64encode(image).decode('utf-8'))
        return self.invoke('/vision/vision_objectr', 'POST')
    
#    def imageTerrorism(self, image, isURL): #url mode failure
#        if isURL:
#            self.setParams('image_url', image)
#        else:
#            self.setParams('image', base64.b64encode(image).decode('utf-8'))
#        return self.invoke('/image/image_terrorism', 'POST')
        
    def imageTerrorism(self, image):
        self.setParams('image', base64.b64encode(image).decode('utf-8'))
        return self.invoke('/image/image_terrorism', 'POST')
    
#    def visionPorn(self, image, isURL): # url mode failure
#        if isURL:
#            self.setParams('image_url', image)
#        else: 
#            self.setParams('image', base64.b64encode(image).decode('utf-8'))
#        return self.invoke('/vision/vision_porn', 'POST')
    def visionPorn(self, image): # url mode failure
        self.setParams('image', base64.b64encode(image).decode('utf-8'))
        return self.invoke('/vision/vision_porn', 'POST')
        
#    def aaiEvilAudio(self, speech_id, speech_url, porn_detect, keyword_detect): #paramter invalid
#        self.setParams('speech_id', speech_id)
#        self.setParams('speech_url', speech_url)
#        self.setParams('porn_detect', porn_detect)
#        self.setParams('keyword_detect', keyword_detect)
#        return self.invoke('/aai/aai_evilaudio', 'GET')
    
    def nlpTextChat(self, session, question):
        self.setParams('session', session)
        self.setParams('question', question)
        return self.invoke('/nlp/nlp_textchat', 'POST')
        
    def nlpTextTrans(self, type, text):
        self.setParams('type', type)
        self.setParams('text', text)
        return self.invoke('/nlp/nlp_texttrans', 'POST')
        
    def nlpTextTranslate(self, text, source, target): 
        self.setParams('text', text)
        self.setParams('source', source)
        self.setParams('target', target)
        return self.invoke('/nlp/nlp_texttranslate', 'POST')
        
    def nlpSpeechTranslate(self ,format, seq, end, session_id, speech_chunk, source, target):
        self.setParams('format',format)
        self.setParams('seq', seq)
        self.setParams('end', end)
        self.setParams('session_id', session_id)
        self.setParams('speech_chunk', base64.b64encode(speech_chunk).decode('utf-8'))
        self.setParams('source', source)
        self.setParams('target', target)
        return self.invoke('/nlp/nlp_speechtranslate', 'POST')
        
    def nlpImageTranslate(self, image, session_id, scene, source, target):
        self.setParams('image', base64.b64encode(image).decode('utf-8'))
        self.setParams('session_id', session_id)
        self.setParams('scene', scene)
        self.setParams('source', source)
        self.setParams('target', target)
        return self.invoke('/nlp/nlp_imagetranslate', 'POST')
    
    def nlpTextDetect(self, text, candidate_langs, force):
        self.setParams('text', text)
        self.setParams('candidate_langs', candidate_langs)
        self.setParams('force', force)
        return self.invoke('/nlp/nlp_textdetect', 'POST')
        
    def nlpWordSeg(self, text):#GBK encoding error
        self.setParams('text', text)
        return self.invoke('/nlp/nlp_wordseg', 'POST')
    
    def nlpWordPos(self, text):#GBK encoding error
        self.setParams('text', text)
        return self.invoke('/nlp/nlp_wordpos', 'POST')
        
    def nlpWordNer(self, text):#GBK encoding error
        self.setParams('text', text)
        return self.invoke('/nlp/nlp_wordner', 'POST')
        
    def nlpWordSyn(self, text):#GBK encoding error
        self.setParams('text', text)
        return self.invoke('/nlp/nlp_wordsyn', 'POST')
    
    def nlpWordCom(self, text):
        self.setParams('text', text)
        return self.invoke('/nlp/nlp_wordcom', 'POST')
    
    def nlpTextPolar(self, text):
        self.setParams('text', text)
        return self.invoke('/nlp/nlp_textpolar', 'POST')
    
    def aaiAsr(self, format, speech, rate = 16000):
        self.setParams('format', format)
        self.setParams('speech', base64.b64encode(speech).decode('utf-8'))
        self.setParams('rate', rate)
        return self.invoke('/aai/aai_asr', 'POST')
        
    def aaiAsrs(self, format, rate, seq, len, end, speech_id, speech_chunk):
        self.setParams('format', format)
        self.setParams('rate', rate)
        self.setParams('seq', seq)
        self.setParams('len', len)
        self.setParams('end', end)
        self.setParams('speech_id', speech_id)
        self.setParams('speech_chunk', base64.b64encode(speech_chunk).decode('utf-8'))
        return self.invoke('/aai/aai_asrs', 'POST')
        
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
        return self.invoke('/aai/aai_wxasrs', 'POST')
        
    def aaiWxAsrLong(self, format, callback_url, speech, isURL):
        self.setParams('format' ,format)
        self.setParams('callback_url', callback_url)
        if isURL:
            self.setParams('speech_url', speech_url)
        else:
            self.setParams('speech', base64.b64encode(speech).decode('utf-8'))
        return self.invoke('/aai/aai_wxasrlong', 'POST')
        
    def aaiDetectKeyword(self, format, callback_url, key_words, speech, isURL):
        self.setParams('format' ,format)
        self.setParams('callback_url', callback_url)
        self.setParams('key_words', key_words)
        if isURL:
            self.setParams('speech_url', speech_url)
        else:
            self.setParams('speech', base64.b64encode(speech).decode('utf-8'))
        return self.invoke('/aai/aai_detectkeyword', 'POST')
    
    def aaiTTS(self, speaker, format, volume, speed, text, aht, apc):
        self.setParams('speaker', speaker)
        self.setParams('format', format)
        self.setParams('volume', volume)
        self.setParams('speed', speed)
        self.setParams('text', text)
        self.setParams('aht', aht)
        self.setParams('apc', apc)
        return self.invoke('/aai/aai_tts', 'GET')
        
    def aaiTTA(self, speaker, format, volume, speed, text, aht, apc):
        self.setParams('speaker', speaker)
        self.setParams('format', format)
        self.setParams('volume', volume)
        self.setParams('speed', speed)
        self.setParams('text', text)
        self.setParams('aht', aht)
        self.setParams('apc', apc)
        return self.invoke('/aai/aai_tta', 'GET')



        


    