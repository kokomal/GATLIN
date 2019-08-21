# coding = utf-8

import json

import gatlin.infra.commonUtils as util
import gatlin.infra.security as sec
from gatlin.nodes.base import AbstractNodeParser
from gatlin.preps import params


# 空的授信节点
class ItemCommitNodeParser(AbstractNodeParser):
    def prepare(self):
        public_req_param = params.genericPackParam()
        util.inject_all_soft(public_req_param, self.context['session'])  # 取初始化参数
        self.pack_method(public_req_param)
        biz = {}
        public_req_param['userNo'] = self.context['session']['userNo']
        public_req_param['token'] = self.context['session']['token']
        public_req_param["bizContent"] = str(biz)  # 业务数据
        public_req_param["deviceInfo"] = str(self.context['session']['deviceInfo'])
        self.context['request'] = public_req_param  # 归根到底目的是为了拼装request参数
        print('ItemCommitQ', json.dumps(public_req_param))

    # 重点在此处理session
    def fetch_resp(self):
        print('RESP OF CURRENT NODE', json.dumps(self.context['response']))
        if 'data' in self.context['response']:
            node_code = self.context['response']['data']['nodeCode']  # node_code
            node_no = self.context['response']['data']['nodeNo']  # node_no
            flow_no = self.context['response']['data']['flowNo']  # nodeName
            self.context['session']['nodeCode'] = node_code
            self.context['session']['nodeNo'] = node_no
            self.context['session']['flowNo'] = flow_no


# 人脸授信节点
class ItemCommitNodeFaceParser(AbstractNodeParser):
    def prepare(self):
        public_req_param = params.genericPackParam()
        util.inject_all_soft(public_req_param, self.context['session'])  # 取初始化参数
        self.pack_method(public_req_param)
        biz = {}
        biz['flowNo'] = self.context['session']['flowNo']  # 取前面返回的flowNo
        session_code_code = self.context['session']['nodeCode']
        if "FACE" != session_code_code:  # 不是FACE
            print("NOT FACE NODE, SKIP!")
            self.context['environ']['skip'] = True  # 跳过
            return
        biz['nodeNo'] = self.context['session']['nodeNo']  # 取前面返回的nodeNo
        biz['nodeCode'] = self.context['session']['nodeCode']  # 取前面返回的nodeCode
        segmentInfoList = [{
            "segmentCode": "FACE",
            "segmentName": "人脸识别",
            "segmentValue": [
                {
                    "fileImageMap": {
                    },
                    "livenessId": "c9765503-2bbc-49ba-afe0-11e545b38473",
                    "detectState": "S",
                    "failCode": "undefined",
                    "faceImage": "",
                    "faceConsumeTime": "12095",
                    "facePartner": "ADVANCE"
                }
            ]
        }]
        biz['segmentInfoList'] = segmentInfoList
        public_req_param['userNo'] = self.context['session']['userNo']
        public_req_param['token'] = self.context['session']['token']
        public_req_param["bizContent"] = str(biz)  # 业务数据
        public_req_param["deviceInfo"] = str(self.context['session']['deviceInfo'])
        self.context['request'] = public_req_param  # 归根到底目的是为了拼装request参数
        print('ItemCommitQFace', json.dumps(public_req_param))

    # 重点在此处理session
    def fetch_resp(self):
        # {"flag": "S", "code": null, "msg": null, "data": {"flowNo": "c49a01bbf7d94d19810168d110f56249", "nodeNo":
        # "200002", "nodeCode": "IDENTITY", "custNo": null, "applNo": null, "lastNode": "N", "applProgress": "12%",
        # "segmentInfoList": [{"custName": "RACHELLE NAVARRO SUGUE", "idNo": "006304154765"}]}}
        print('RESP OF CURRENT NODE', json.dumps(self.context['response']))
        if 'data' in self.context['response']:
            node_code = self.context['response']['data']['nodeCode']  # node_code
            node_no = self.context['response']['data']['nodeNo']  # node_no
            flow_no = self.context['response']['data']['flowNo']  # nodeName
            self.context['session']['nodeCode'] = node_code
            self.context['session']['nodeNo'] = node_no
            self.context['session']['flowNo'] = flow_no


class IdcardUploadNodeParser(AbstractNodeParser):
    def prepare(self):
        public_req_param = params.genericPackParam()
        util.inject_all_soft(public_req_param, self.context['session'])  # 取初始化参数
        self.pack_method(public_req_param)
        session_code_code = self.context['session']['nodeCode']
        if "IDENTITY" != session_code_code:  # 不是IDENTITY
            print("NOT IDENTITY NODE, SKIP!")
            self.context['environ']['skip'] = True  # 跳过
            return
        biz = {
            "bizType": "OCR",
            "fileSuffix": "jpg",
            "fileKeys": [
                "idCardImg",
                "portraitImg"
            ],
            "idCardImg": "\/9j\/4AAQSkZJRgABAQAAAQABAAD\/2wBDABALDA4MChAODQ4SERATGCgaGBYWGDEjJR0oOjM9PDkzODdASFxOQERXRTc4UG1RV19iZ2hnPk1xeXBkeFxlZ2P\/2wBDARESEhgVGC8aGi9jQjhCY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2P\/wAARCAGVAqkDASIAAhEBAxEB\/8QAGgAAAwEBAQEAAAAAAAAAAAAAAAECAwQFBv\/EACkQAAMAAgMAAgEFAAMAAwAAAAABAgMRBCExEkEFEyIyUWEUcYFSkaH\/xAAYAQEBAQEBAAAAAAAAAAAAAAAAAQIDBP\/EABkRAQEBAQEBAAAAAAAAAAAAAAABERICMf\/aAAwDAQACEQMRAD8A6djJHs87oYg2CKGIGwQDSBgADQtgIAJZTZKIKQxINlQx7J2GwKDYhN9gUmPZCY9gVsWxAUUholMNgVsNiAIexA2IKpMeyRhD2GxMWwHvSPK\/Kc5Y4a2dPO5SxQ+z5P8AJ8x5raT6LJo5+XyHmyNtmUyKVtmqWkdJGSekZUyrozphCbCJd0khes9L8bxdtVSFV1\/juKolNo9NdIjHKiUkU2YaNsQAiBouUKZNscbAInb0l2bzKxrb9BOca\/05s+ffSLiKz8j6RzzNZH2Vjxu3tnVjxqUAYsKnRrvQnWkcfJ5ahPsitc\/JUJ9ni878h6kzHm8502kzzqt29tlkS08mSsjbbJSGkVMm2dEo0mQSKXRQ\/j0Y5UbNmd9kHPolo0tGbAkcvTBoAr0OHm012evgybSPnsNaaPY4l7SOdjUenjo68NHBjo68FEadsdmiRljZqvAlMQwKhAAMKQ0gSGQADJYQmyPWVQpXZYVcI0JlDZuMJpnPlro2yPo5M1CrGNvbJ0G+w\/8ATna3HoaYtHb+ihfoIvDPTj7A6ngE8A4XpzMEbvAyXgaJzTWew2U8TF+m\/wCiZV0ti+huWS00Amxon7KRFUIQFQ0CEMBiDYAMWx7EwHsZCKTKGGxABWw2TsWwK2CJGmBWw2INhDMuRmWOH2PJaiW2zwfy35DSaT7EHL+X57puUzxu6ZWS3kptscSdJGbVQtIV0OnoyqioVMhsGy8OJ5LS+gNuHx3ktNro97j4lEro5+HgWOV0dfyMWtL2NGaoueyKoqUCRviw77fSAWOG\/wDo0q1C0hZMihaRy1dZHpeFQ8mV09IvFhb9Kw4ftnSkpRLQphSgqkkK7UrtnnczmqU+wrXlctSn2eHzOa7ppMz5XLrI3pnJ69mpGdNt09saQJGkyaQpktIakpIoSXQMbZFMAbJbBslsBV2Y2tGuyaWyDNMrRLWmXDCnjXZ6vDfSPPxxtnp8WdJGPTUduM7cBxYzswMyrux+GqM8RqkAbGmLQIBiDY0gDQDABCY2TQEvtlwiUuzSUa8xiqJplGds0jLLRx5Htm2ajnp7Zn1WvMLQa\/7GhmG30AAB3cgLQAAaD4oAIE5T+hPGv6KADP8ASRLwJ\/RsAw1z\/wDHRL451AyZF1xvAyHgZ3aD4ocw6ee8VL6E4ej0HCJeJE5XpwaaA7XhRLwr+icHTjbBM6XgRP8AxycrrENmrwsTwsZTUbFst42J42TKanYbBy0LTGKex7J0wCK2J1rslvRxc7lrHL7Ax\/J85RDWz5jk53mts25\/LebI\/wCjkS2bkS04k08QJaRNs0ym2Ztjpk+sBzLppI9bg8ZSk2jn4PG202j1ZSidGbWldShfLsiqEmZVtLNY7MYTb0l2duHEoW69LIjTDjS7v\/6Ky51K9MMuf49bMUqyVtl+J9W6rLX+HThw69Jw41J0J6M1T6SM8uRQt7FmzKF6eRzedra2BrzOd8U+zxOTyay0+yc2eslPsy0bkS0JbLUgpLUlQTJcoFJa6KFoGwbIbAGyWwbJbIBslsGxFUbAAIiKQp6ZoS5CurjdtHqYJ0keVxf5I9njr9qOdajaEdeFGOOTpxT4RXViN0YYkbrwBiaGhhEaGh6DQUbDYgAGyGU2SEVCNUiYRejpGU0c+V6RtZy5qFRhlrsyKp7Ykjna6SGhjS2V8SK9sBAd3IxAADEAAMQAAwEADEAEBsNiABgAihiAAAWhgQToPihgAvihOEUIoh40S8SNQJgxeJEvCbgxhrlyYNro8rm\/jXm2uz3mQ5T+hhr5G\/wD3vszf4Wp82fXOF\/Qv0pf0VHx1\/isiXRz5Pxmbfh9tXHh\/SM3xYf0ga+Ir8bn\/wDiXg\/G5flupPsnw4\/oa4cL6FXXgYuNWOfB1Ff0e\/8A8Sf6E+FP9GcXXz\/wr+hxjqnpI92uDP8ARjkxxiT0Tk1zYcSxLfrFmz66XpGbPrqTGZdPbKi4l29s68UKUYwvijT56Jitt6Rjm5ChemOfkqU+zyeXzd7SZMVtzef6kzy8mR5K22TVOntgkakS0JFTI0i5kqCZLSGkUAhNg2Q2UDZLYNktkA2S2DYgAAAKAAaQQJFKdlRB04MG34S1T4mDbTPXwY9JGXHwpaO3HBitRUSbwtEzJpKIrbGbIyhG0hDEx6DQUJD0AAJoTKZLYEUE+iZUIvlmtYRT8FKCn0bZY5X0cWajpzUceR9krUiCkhIuUc2zlF6CUVoD1G9DT2Z2xwzu5LAQAMAAAAA2AAGwAAAAAQAABsAAAAAAQAAAIAAAAAAAATENiYCYmDEwiWIbEFJvQk0zHkW10h4Nv0I20UkCRSQCSB9A3pdnHyuWoT0yCuTyFCaTPH5PJd00mLPyKy1pMiMf2wpRG3tm8zoJSQ3SSChvRz5+QpXpHJ5KlPs8rkch23phF8rlum0mcjbbD0aQCSLmRzJpMlCUlpDSGQIGxNkNgDZLYNktgDYgEFAhiAAGkUpCEpNMePZWPE2ztw8f\/AMsWLs7cGPX0Vi4\/wDh148H+GbK1KMUnTCHjwf4bTi19Gcq6Uo0lAsTLWNjKaqUXJKhlJNDBaAnse2BQmLYvkQNkUN0S2FCW2awjOEbyjcjFPwyyM0pmGWjSOfNXpyvtmua+zJM5+q6SGkaSiZRrKMNGkVoSK0Ed1hDKtdET6ehxaACGFIBgAAAgJrocsVDkIoBBsKBiAAAQbAGwRNMcgMAAAEMQAAAACBsWwBiGxMBMlsbZIA2IA0BzZu6NsE9GeRfuNsX8QNBVSlbYrtQts8zm83W0mRGnM5qlPTPKy5qy170TVVlrbNIjSClGM0S0NLRN2pQDqlKOLk8pSn2Z8rl62kzzMuV2+2BWbO8j96MgRSQCSLmRzJakAmTRISQ9lBvRLYNkNkA2S2DYgE2IYgoEwYAIaQ0i5nYCmdm2LE2y8OFs7sHH19BEYOP\/h24sRWPEdGPGAY8f+HTjx6Fjg6IkBxJpMhMmiQApKUjSGAlKK+KBFAT8EL9MsBis\/0xPGbCZMNc7xkOdM6KMn6MNEI0RMooCaZy5q9OjIzlyvYo5MrbZMpnQse2aTgX9GLG9YTs1k2WEpYScnTJD2a\/pB+kOTXZXhlvTNn4Za7OzkufChLwYUCAAAAGBNCkdCkIoQxBQAAACAAJsJYWKQix7EAUbBgLYD2IQbAmwlitiTCL2JsWxbAGxDDQUtD0AwObLv5dDWVY47fY89zCf9nkcrlPbSZEa8zm7bSZwPeStsFLt7fZtMaClEaRfgeGWbMoXoFZMqhdnm8vmepMjlcve0mcFU6fZQ7t2\/SUgSLSIEkaTIpk0mQBSXoEDZQbJbBshsAbJbBsRAMQAwoE2DFoIBpDU7NYxtsKmI2dWHBt+F4OOd+LDrXQGeHBr6OvHj\/wqMZ0Y8YROPH\/AIbxGiog0mQCZNpkUyaSigSLSBIaRA0MEMoSKQhkUAAFAJjJZETTIXo6YSgKQn4Mm2FY5Wc9PbNcrMfslF41s3hGWNG8+EFJFaEhlBoNAMo1Zm\/TQzpdlRcjFPgwAAAAAAAVEyOiZCLEABQIYgAAEAqFIUKQLAQAMQAACBi2BNikLYpCLEAwoAYf9hC0Y8jkTil9kcnlLHL0zxuXyqytpMinzPyHypymYY18+2c7xP5bZ2YVpAXM6Q96BtI5uRyVKemBWfOoXp5XK5TptJk8jku20mc3voA22+wSBIpIASLmRzJpMgKZK0PwWwAlsGyWyhNktg2IA2ACZFGxMASAEilI5k6MWF0wIx4nT8O3Bx\/8NcHH19HVGPSCIx40vo6ceMUY+zqxxr6AUYzeYCINZkBTJpMjmS0gEkWkCRSQAkVonZSANDAAAYAVRoAAAIplMimREv0qSV6WvABmWRmjMMrAwyMiV2O3tjhEabQjWUZwaygigAZQhgAGpnfpoyLKhy+iiIKANjEADAQAKvCZ9KZP2BYAJgDEMQCAAAml0KfSmSvQixNDQBSENksAYtgxbCJsUsLCEBaGhA6UrbAptJbfhxcvmKE0mZ8zmqU0meTly1lr3oKrPnrLXvRMQOMZqlogwyLRUUkieRWls4MvL1vsDp5PKUp6Z5efO7b\/AKJy5XkZACHoClIBMmikJk0SKEkUgE2QNshsGyGwBslsGIAYbEBQCApIBJGkRscY2zswcb7YVnh4+9dHfhwa+jTFh19HTGMiJjGbKOi4xmnwAzxx2dMSLHBvMgKZNJkEi0gBIpIEigFooSG\/AI+zSfCF6WgAYgKpiGBAAAgEzKmaUzF9sIuTQmF0U\/CCKZzZWb2zmyPsqsn2zTGiEbY0RWko0SJktFQbFsbEuwKD\/wAANFGxFosm\/AiYLMprs0XYAAwAQAAA\/CPstkP0IpAwQMKQAxAAAIArwlelMjfYRoJsSBsAbJ2NslhQIYATXgoHRneRYltsI2qlC2zzObzktpMw535LW0meY8lZb2yLjarrLW2zSMeicaNdgMjJkUL0nLlUL083lcve0mBXL5O9o8+q+THVOn2IBD0GtlKSgUmkyEyWkQJIoBNgNsimDZDZQ2yGwbFsgBbACgAEi5kgSnZrjxNvovFhdHfg42tdFGeDj+dHdixJLwrHi0bxBAoj\/DeIHEG0yUTMF\/EtSGuyIeOTVSKF0aJBQkNIaQ9AIY0h6KpIK8KJoImV2aEyUFAhgAAAEAJgJgTZml2XTFKAuQpjXhNMiMsjOW32bZWYPthTk3hGUI3lAXKKRKK+iommOeya9KgCg0MCjUVroomvCDJT2apEL00KEAAAAAAJkP00ZnXoDXgMEDAQAACAYgB+Gb9LZm\/Qi0wbEDClsBDQQAMxz55xS++wHmyzjlvfZ4P5L8l20mT+S\/IN7Us8Sqq8m6ZlrHUreR7bN8SMMS0kby9AdEULLnUL05snIULpnFm5Dt9MqNOTyXTaTORvb7AAAaWwSLmShKS5kcyaKQJUlaGS6IBvRDYOiGwBslsGxAAgAoBpAkaxDbAmY2dOHBt9mmDj79R248KX0QTgwJa6OyMeh4sZ0RjKJiDaIKiDWZIJmTSZKmSlICSFrs010TrsqLhFpCldFJEUaGGhhQhhoeioRNFmdegOShT4MgYgAABgACExksCK9HKF9logZlbNGzHIwrDIzNdsq3sJQGmNG0ozhGsoBob8BIVeFRP2XPhC9NEFADAo1CvAE\/CCF6WjP7NEVAAxAAAAAZ0WRQDkZMlAIQxMBNiBiAb8Mm+zRmVehFoZKY9gGg8F8jj5nNnEmkyDbkcmcUvs8fkZ6zt6fRnfKfJrSZt+ksePbIryeZOn2csLdHRzb+eTSIxRpbYVpK0iMub49InLm0tJnLVOmVFXkdMgPBgIaQ1JcyUKZNJkcyWpASQ34DeiaoAbM2wpktkA2S2GxMA2JgNIBFJbHMm+LC6+gIx4nR3cfjedGmDja10d2LFr6Azx4dLw2nH2azjLiOwHijo3mBxBrMgSpNJkcyUkEJIpIaQ0gpNdCldlNdClFRaGAyKEMSGAwAAoZm\/S34QvQi14ALwAoAAAQwEEDIopkUAkWTJTIqaZhkfRrZhkYGT9LhEI1hAaQaIiTRFDQq8KRNBEz6WiUuy0AAAyiwYARWb9LnwivSpfRUUAAACAAAiihUApKZMjYCABAIQ2SwBmVemjM6fYRSfQbJXgAc3MzuJej5\/lfr8rL8Z6R9FnxK0cscVTW9ExWX438ZOCFVv53\/8AhpzY60dX6nxnSOTkZUk22DXk5cClts4s2XXSOrnclNtJnm0\/k9sBNumAAAelKQlFzJQTJpMhMlpEAkDegbIqgCmZ1QUyGwBsTE2LYDEBSQCSLmNlRG2deDjbfYGeHA6fh6ODj6XheHAlro6ox6+gJx49HRGMcYzaYKJUdDiezT49FRIRUyaJApKSIoSKSBIeigSHoaQATSCUOhyiIeg0MAoAACmAhgTQl6OhSEUAAFIEAAMTAQQMzbLZk67IrSRsmWNsCLZzZO2bZGc9PbAJRtKM5NZQFyjREyUihkUymS\/QhooSXQygGIANRABFZ2hwOxSVFAMAATGJgIVeDFXgEJlEr0oBMTY2SwBslsGyWANmdPstozr0IufBsmX0J0AUZVpFVRycnkKU+yBcjMpTPH5vL3tJj5fL3tJnm5L+T9CpunT22QwbBLYB6OUNSaTIBMmkyEyUUHgmwbIqiAdEVQqozbAbZLYNiAYIEi5kBKTWIHGM6cOH5NAXxuPv6PQw4UkHHw6S6OuMYExBvEFRBrMlCmDSZGpLSAhoqEDRcICkikgSK0QJIaQaKAQaGAGbLldEv0ufAGAAAAAAAAAE0wkVejkChAAUCGIAExiYE14ZNdmlAkQKUOuitEWwMcjMfs0yMzQFyjWURBrKApFISRSKE\/CfsqvCZ9AtACGVAACIrXQhiKJvwmPS68In0iNABAAgYCABPwYn4Bn9lkP0pFAS0WSwIaJLZOwEzG+mbMxysAVdE1WiXWkcXL5SlNJhGnJ5SlPTPG5XLdNpMnk8p032cOS9kUZMm2ZN7BvYJBRrZUoEjSZCCZNEgmS\/AEhN6BsiqAKoyqh1Rm2ANkjDWyhaGkNSazBBMwb4sWx48f8AZsv2+FAsR0YJcvwOPjdPs9DHx9rwBYLXWztxpPw5Xxmn0dXGhpdgbTJqpCUWkQJSVopIeijJrs0hE\/ZpKIGkPQ0gKBIegAgQMYn4FSvS0SvSghiAAoAYAIGMT8CM36WiH6UgGAAFAhiABMZLCJY0hfZSIofhnkZozDKwMbfYpB+lQgLlGsoiUaIopDBDAiglBQ5QFIAGEIAYBWohiKhUZr01a6MmuyC0ALwZQhDFogQmVoGgMn6UvBV6NFAxMoTAzZJoyGBLOfNalPZrlyKE22eRzuau9MgfK5alPs8jk8l032Rnzu2+zluwHdme9hvYJACRcoFJpMhRMmkyEyV4AeE1QVRlVBDqiHQnRLYA2SMNALRSkcybY8bb8AmI76OvBxm3to14\/F8bR2zCxoDm\/wCNr6NMeCftGyua6H8V9AKJUPo7+OtpHJjxbZ6OCNJAWoTNJlIakpSUNIpIEikiAQMegfgEJdmiXRCXZogAYAFMAQwFomiiaAUlCkoA0AAACGAAKhk0BC9LRMosBAAAAmMAERRbIoIS9KQkhkUqZz5WbWznyMDP7NIRCXZrKAuUaSiJNJKGhsAfgRD9Kkj7NEgpgABCAACthDAqEzKumamd+kDl7GKR7AA0AALQMYmUZ0CCvRIBsTBsTYCbMM+ZY5bbDkZ5xp9nhc\/n7bSZBfO5\/qTPHzZ3TfZOXM6b2zCq2AVeyPR+jSASRcyNIuZCiZ7NJQKSvAAmqFVGV2A6ozdCbEVA2ICkiBJFzI5k6cOB010BGLC39HdxsH9o2w8bU+G+LHqgLxYtIeeUpOrHj6MeXibl6KPNWRK\/Ttwz80eeuBlrJvbPR4vHyQ1sg6cWHTR24p0iMc6XZ0QghpFJAkUkVRoeg0PRAaE0UJgTK7LSJldlgAAAUDAAERXpZD9AqRikYDEMAAAAAIstmdBBIwkAoAAAAAAEyH6XRAQ0hggogyyHPb7N8jOavQpz6ayjOTWQLktEyWihoVDJoBL0tEz6WAAABCABhWogAqAys1MshA5KIgsAFsBMB7JbBslsommLfQWyUwKbMsuT4y2U2c\/KrUMg8j8ly3trZ4uXK6b7Or8lf7mea62wp1WxegUkECRSkak0UhSmTRToEivAheEVQVRlVAFUZtg2IKA0CRcoBKS5jZWPG6fh38bi\/wBoIy4\/GdabR6GHjpfRthwfFeG8Y+wFOP8AaER+86VH7SIn94G8T0O9fZcT0Rnh+oCseOX9IupmVvRz4s3wXY6yPK+vAB518tI68L+SOB4dPZ28b+IG6RSQJDQBoNDDQCFQyaAclCkoAAACgABADM36aUZ\/YFoAQAAxDAAAABmdelsh9sIa8AYBSAAAAYMTYE0xIGCIi0TT6GRb6CscjMfs0t9kJdlFQjWURKNZRBUlISKRQE0WQ\/QhyihSigoEMAhCGAVoAAVARaLJsgmSmTI2UJgDJYA2Q2NkgTZKY7ZlVaQFXWjk5V7l9l5Mhy5b2QeJ+Rn9zZ5+j2eXgdJs8vJHxoDNIuUJI0lAOZK8AToinvQqsiqIdFQ6rZm2DDQUhpDSLmd\/QQpnZtiwumXh47r6PT4\/FS10FZcXia1tHo4sCX0XixJJHRMaCIWPoqY7NFPRUT2UHx\/aZzP7zp1+0ylfvINonoqo+SHK6LSKOV8VN+FxgUnQkDXRBxcjSejfjL9qIvF8r2dOKPigLGgQwAAAKTIfpo\/DP7CLkYkUFIAGAhiGBNEr0qhIIZLrRZDnbCnL2UKVoYAAAwFRC9KoSCGIbAKQAAAyWNiYRLGiS0RQzK2aUY5GBjXo5RL9LgDSUWkTJoihoaBDQAyPsuiF6EWhggCgQ2IIBDF\/4FbCACoCbKIvwgmWVszn0psAbJbGyQEyWx09Gbe2UKns581fFHQ\/Dj5W34Ec+TI2wxY3bHiwOn2ehx+P50ZacmTifKPDxedwqmnpH2ePjKl4Ycz8bNw+is6+FcNPsa6PS\/JcJ4bfR5tdBSdaIqgqiGyAdEtgCRQIpIEjSIb8AUzs6+PxnTXRpxeI6abR6uDi\/FLoDLj8bSXR2Y8WjSMejWYCpmDSZLmS1IRHx6HE9ltBCAeujJLVnQ10Y6\/eBtK6L0KF0VoASE\/BvpGFZP3aA1lGiRnj7RoADBDCkAwATI+y6IXoRaAAAYAAAAABFDkT9KkAAYgoAAIABiKIoEFAghgABQAAwEyKKbIbCEi0SiiKi2YZGa5Gc9solds1hGcm0og0kpClFIoaGCGETQp9CghBVgMQQCGACENgBqJgxFAyL8KZnb6IEmMiWNsAbIq9Cu9HPmy6KKvL3rYTWzhebs6MD+RYldHpNY9mko0iNsIzxYO\/Dtw4P8Kw4f8ADrxxoijFj0VlhfBlrUo5uRyElrYHhfmOMrT0j5fl8dw30fX8zKq3s8HnfB7XRFeBW0SdeTA6baRjWGk\/AuMki5RSxv8Ao3w8arfgGePE7ekj0+JwfG0dHC\/H602j1IwqJ8CMOPxlK8OpYy4k0UgZKC5kv4h0gBSUkNdlJAQ0OUOhygG10Y6\/cbtdGL\/kBvHgxR4F2p9AWR6lnEm3kOqrVIxhL5AdONdGhMLooAGABSAAAVCkKHIFAABAAAFAMBMgh+loj7LRUMAAKQwAAEwEwJr0aJ+ykEAAAUCYxMCWQXRH2QUgY0iaAyyMwpmuRmWtsBwjaURCNZQFItCSKRUAxBsCa9Kkj7LXgDAACgAAIBAAGmxMWxNlA2Z2ymzPI+gJTFd6MqvTIvJ0wM8+fT9MMmT5Ix5Ft0XiXzkqMp22d3G60c6wv5HdgwtJAdGOfkdmHEYYZ1o7sa6ILiNGm1KM3alHJyOTr7A15HJ0tbPM5PK0ntmfK5alNtng\/kPyXqT7CtvyH5HW0meNk5d5L96M6yVmrb2dfF4TtptEG\/Ej9RLaO1cFV9G3F4nwS6O6ISJi681fjVv+J04OBM\/R2zBakqIjEpXSKcmikGgFEmmhQin0gFoxuG6MuTzVifpnxub+tXQHdE6RpomO0XoKhlSiX6XK6CG10c7X7jofhg\/5gbT\/ABOXkb2dSekc2fvegrB38Vps14z+T2cWSLd\/4d\/EjSQR1yuihSMAAACgQ9ABFFSQ\/S5CGAAAAABQKvBk0ESvTQhelgAAAUAAMAJrwomvAiF6UKfRhQIYAAmAmwiaYShMqSB6M7ZozHIwrHIyZC32OEBpKNETKNEUNFolFIIBMZNAJeloifSwAAAAFsYgAAEFU2S2DZnVFQ6oxy30LJk0jlzZdpkGebPpim\/kcl1ujp4y3o0lZ5sf2a8WW\/o6f0fma4uOp8ArHhXT0dGOV4PFH0bxjS7IHGM0dqERWRSjkz5\/9A0zcj3s8zl8tQn32ZczmqE++zwOdzqyNpMK15\/5B02kzznNZa7+xY4rJf3s9fhcHem0RXPw+A3ptHtcXjqUujTFx1E+G+OQhzGjSZKmS0gEpKSGkVoKSQNFITXYQ5QWtoa8ObPkqX0gOLncT5vZt+P4ixpMzzZbr6Onh09LYHYlpDBAwqPstIlemiQQq8Od\/wAjprw59bsDPkZnEdGXGy\/qPs6c2FXHaOFQ8d9BXZkhepFYTD9XrsvDl2wOxeDFL6GEAAAUCYxMCPstEL00SAAGAQgGIAJopk0ASUTJQUAAAAAACFRRFhCkbFIwoAAATJopk0EQWvCUWiKVMwyM1pmGRgZP0uEQvTaEBpKLRMorRQ0UShoIZNFEUFElkwUAAABAJjEAgAYVjV6Rz5c2vsjNnSOHNmboqNsubZC3SZlKdHTggqOW8TVeHXxcb12bLCn6b48WkQOI0jfEt\/QRBskpRBSlJE3lUojJl0jjz8jS9KrTPn19nlc3nqU9Mw5\/5BSmtnjZs1Z696AfL5tZaaT6IwYXkfhWDh1kpf0ezwuCpS2iKy4fAS70ethwqF0iseJSvDaZAzcmmOBuS4kIaRSQ0ikgEkPQ9D0FToX2WyfsIb0kc+TJD3to2ypuejyOTNTT7A6v2U+uzowY9HLwI3ps9OZSQAkDGJ+BSn0siSwia8ZhP8zbLSmXswx0qoK3a3JxZ6mX2dl\/xPN5OOrp\/wBBDWSbekdXHwpdnFgw\/Cu2enh\/igrRLQwAIAGIAJosigpT6WTJQQwAAAQwCloh+lkP0IclCkYUAAAMQAANmdPstmdehDnwYl4DCgABgJkUWyGQCKFI34BnbMLZrbMKe2AQuzeEYwjeQLRSEikUGhgACZD9NGZ\/YFyMSGAhgAQCYAQAgAo+dyZXTJ020KYbo7MWHaKgwQdWONCx4\/idERsBzj2bY4HjjRo2kiKOkjPJl0Tky6OHk8lQntlF5+QpTbZ43P8AyGk9Mx5\/5D1Jnk1krLf2QVmy3ls6eHxatra6NeHwnbTaPb43EUJdBWfF4ilLaO6I10XEaLUgKZLSGkUkBDRcIGipQQ0h6GkAUIeg0MITJXpb8JS7Cm1tHNn482b5L+EnFXJbrWwjTBjWN6R1y+jhjLtnZje0BYq8GTQBJZMlBXPyU3L0cWKqi+z0M\/hjGJUBlfM10CfzWy8vDVfRH6VY10EZKa+Z6GFftRx\/Jy\/Dpw22gOgBIYAAAFBNFE0AQWTJQQAAAIAAKGR9lvwhBFIYAFAAAAAAAmZvtlvwj7CKQAAUgYxMCaIXpVMlEFoVDRNgY5GZesvIyZQFwjaURCNZRQ0NAkMoAGgIJoj7LomUBaAACAQAAADEFMQAB4mPHPTOzHKQAWsNplM3xSkAEaavpGOW2AFHDyctTLZ4fP5NvYAB5bXzrtndwuNDab7ACK93iYplLR2SkAAaSi5QAQVoaACoT9LlAAFAABTQwAIVeEoACuPn5HMvR5f6lb3sAA6eHPyrbZ6+NakAIKJr0AKhooACsMw8PgABqyGk\/UABEVjlvw0iEl0AAWAAFAwABE0AAOfCgAAAACAAABUSvQACvoAAKYgAAEAECrwhegBRQAAQCoACs6CQAgozsAAwr0cAAG0miACopAAFU0AABFBPoAQUAAACAAAWgAAAAA\/\/2Q==",
            "portraitImg": ""
        }
        public_req_param['userNo'] = self.context['session']['userNo']
        public_req_param['token'] = self.context['session']['token']
        public_req_param["bizContent"] = str(biz)  # 业务数据
        public_req_param["deviceInfo"] = str(self.context['session']['deviceInfo'])
        self.context['request'] = public_req_param  # 归根到底目的是为了拼装request参数
        print('ItemCommitQId', json.dumps(public_req_param))
        # 重点在此处理session

    def fetch_resp(self):
        # {"flag": "S", "code": null, "msg": null, "data": {"fileNameCodes": {"portraitImg": null, "idCardImg": "FN026a76f31ca6485fa895d98597f343dc"}}}
        print('RESP OF CURRENT NODE', json.dumps(self.context['response']))
        if 'data' in self.context['response']:
            pass


# 修改密码（交易）
class TradePwdNodeParser(AbstractNodeParser):
    def prepare(self):
        public_req_param = params.genericPackParam()
        util.inject_all_soft(public_req_param, self.context['session'])  # 取初始化参数
        self.pack_method(public_req_param)
        biz = {
            "password": str(sec.encrypt(bytes(self.context['environ']['newtpassword'], encoding='utf8')), 'utf-8'),
            "pwdType": "T"
        }
        public_req_param['userNo'] = self.context['session']['userNo']
        public_req_param['token'] = self.context['session']['token']
        public_req_param["bizContent"] = str(biz)  # 业务数据
        public_req_param["deviceInfo"] = str(self.context['session']['deviceInfo'])  # deviceInfo需要转换
        self.context['request'] = public_req_param  # 归根到底目的是为了拼装request参数
        print('ItemCommitTPwd', json.dumps(public_req_param))

    def fetch_resp(self):
        print('RESP OF CURRENT NODE', json.dumps(self.context['response']))
        if 'data' in self.context['response']:
            pass


#  身份证提交
class ItemCommitIdNodeParser(AbstractNodeParser):
    def prepare(self):
        public_req_param = params.genericPackParam()
        util.inject_all_soft(public_req_param, self.context['session'])  # 取初始化参数
        self.pack_method(public_req_param)
        session_code_code = self.context['session']['nodeCode']
        if "IDENTITY" != session_code_code:  # 不是IDENTITY
            print("NOT IDENTITY NODE, SKIP!")
            self.context['environ']['skip'] = True  # 跳过
            return
        biz = {"applNo": "", 'flowNo': self.context['session']['flowNo'],
               "nodeCode": self.context['session']['nodeCode'], "nodeNo": self.context['session']['nodeNo'],
               "segmentInfoList": [
                   {
                       "segmentCode": "IDENTITY",
                       "segmentName": "身份信息",
                       "segmentValue": [
                           self.context['session']['idcard']
                       ]
                   }
               ]}
        public_req_param['userNo'] = self.context['session']['userNo']
        public_req_param['token'] = self.context['session']['token']
        public_req_param["bizContent"] = str(biz)  # 业务数据
        public_req_param["deviceInfo"] = str(self.context['session']['deviceInfo'])
        self.context['request'] = public_req_param  # 归根到底目的是为了拼装request参数
        print('ItemCommitIdUpload', json.dumps(public_req_param))

    def fetch_resp(self):
        # {"flag": "S", "code": null, "msg": null, "data": {"flowNo": "a456abb1c4cb4b849faeb16b9834a2da", "nodeNo":
        # "200003", "nodeCode": "PERSONINFO", "custNo": null, "applNo": null, "lastNode": "N", "applProgress": "25",
        # "segmentInfoList": []}}
        print('RESP OF CURRENT NODE', json.dumps(self.context['response']))
        if 'data' in self.context['response']:
            node_code = self.context['response']['data']['nodeCode']  # node_code
            node_no = self.context['response']['data']['nodeNo']  # node_no
            flow_no = self.context['response']['data']['flowNo']  # nodeName
            self.context['session']['nodeCode'] = node_code
            self.context['session']['nodeNo'] = node_no
            self.context['session']['flowNo'] = flow_no


class PersonInfoNodeParser(AbstractNodeParser):
    def prepare(self):
        public_req_param = params.genericPackParam()
        util.inject_all_soft(public_req_param, self.context['session'])  # 取初始化参数
        self.pack_method(public_req_param)
        person = self.context['session']['personal_info']
        session_code_code = self.context['session']['nodeCode']
        if "PERSONINFO" != session_code_code:  # 不是PERSONINFO
            print("NOT PERSONINFO NODE, SKIP!")
            self.context['environ']['skip'] = True  # 跳过
            return
        biz = {"applNo": "", 'flowNo': self.context['session']['flowNo'],
               "nodeCode": session_code_code, "nodeNo": self.context['session']['nodeNo'],
               "segmentInfoList": [
                   {
                       "segmentCode": "PERSONINFO",
                       "segmentName": "个人信息",
                       "segmentValue": [
                           person
                       ]
                   }
               ]}
        public_req_param['userNo'] = self.context['session']['userNo']
        public_req_param['token'] = self.context['session']['token']
        public_req_param["bizContent"] = str(biz)  # 业务数据
        public_req_param["deviceInfo"] = str(self.context['session']['deviceInfo'])
        self.context['request'] = public_req_param  # 归根到底目的是为了拼装request参数
        print("PERSONAL-INFO PARAM", json.dumps(public_req_param))
        return

    def fetch_resp(self):
        # {"flag": "S", "code": null, "msg": null, "data": {"flowNo": "a456abb1c4cb4b849faeb16b9834a2da", "nodeNo":
        # "200003", "nodeCode": "PERSONINFO", "custNo": null, "applNo": null, "lastNode": "N", "applProgress": "25",
        # "segmentInfoList": []}}
        print('RESP OF CURRENT NODE', json.dumps(self.context['response']))
        if 'data' in self.context['response']:
            pass
