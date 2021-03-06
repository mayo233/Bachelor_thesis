# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from ddynamic_reconfigure/TutorialParamsRequest.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class TutorialParamsRequest(genpy.Message):
  _md5sum = "d41d8cd98f00b204e9800998ecf8427e"
  _type = "ddynamic_reconfigure/TutorialParamsRequest"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """"""
  __slots__ = []
  _slot_types = []

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(TutorialParamsRequest, self).__init__(*args, **kwds)

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      pass
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      pass
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from ddynamic_reconfigure/TutorialParamsResponse.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class TutorialParamsResponse(genpy.Message):
  _md5sum = "2b2d98973833896677e387258d00296b"
  _type = "ddynamic_reconfigure/TutorialParamsResponse"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """int32 int_param
float64 double_param
string str_param
bool bool_param
int32 enum_param
"""
  __slots__ = ['int_param','double_param','str_param','bool_param','enum_param']
  _slot_types = ['int32','float64','string','bool','int32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       int_param,double_param,str_param,bool_param,enum_param

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(TutorialParamsResponse, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.int_param is None:
        self.int_param = 0
      if self.double_param is None:
        self.double_param = 0.
      if self.str_param is None:
        self.str_param = ''
      if self.bool_param is None:
        self.bool_param = False
      if self.enum_param is None:
        self.enum_param = 0
    else:
      self.int_param = 0
      self.double_param = 0.
      self.str_param = ''
      self.bool_param = False
      self.enum_param = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_id().pack(_x.int_param, _x.double_param))
      _x = self.str_param
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_Bi().pack(_x.bool_param, _x.enum_param))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 12
      (_x.int_param, _x.double_param,) = _get_struct_id().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.str_param = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.str_param = str[start:end]
      _x = self
      start = end
      end += 5
      (_x.bool_param, _x.enum_param,) = _get_struct_Bi().unpack(str[start:end])
      self.bool_param = bool(self.bool_param)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_id().pack(_x.int_param, _x.double_param))
      _x = self.str_param
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_Bi().pack(_x.bool_param, _x.enum_param))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 12
      (_x.int_param, _x.double_param,) = _get_struct_id().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.str_param = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.str_param = str[start:end]
      _x = self
      start = end
      end += 5
      (_x.bool_param, _x.enum_param,) = _get_struct_Bi().unpack(str[start:end])
      self.bool_param = bool(self.bool_param)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_Bi = None
def _get_struct_Bi():
    global _struct_Bi
    if _struct_Bi is None:
        _struct_Bi = struct.Struct("<Bi")
    return _struct_Bi
_struct_id = None
def _get_struct_id():
    global _struct_id
    if _struct_id is None:
        _struct_id = struct.Struct("<id")
    return _struct_id
class TutorialParams(object):
  _type          = 'ddynamic_reconfigure/TutorialParams'
  _md5sum = '2b2d98973833896677e387258d00296b'
  _request_class  = TutorialParamsRequest
  _response_class = TutorialParamsResponse
