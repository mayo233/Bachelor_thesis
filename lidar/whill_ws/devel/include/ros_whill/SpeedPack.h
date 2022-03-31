// Generated by gencpp from file ros_whill/SpeedPack.msg
// DO NOT EDIT!


#ifndef ROS_WHILL_MESSAGE_SPEEDPACK_H
#define ROS_WHILL_MESSAGE_SPEEDPACK_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace ros_whill
{
template <class ContainerAllocator>
struct SpeedPack_
{
  typedef SpeedPack_<ContainerAllocator> Type;

  SpeedPack_()
    : speed(0.0)
    , acc(0.0)
    , dec(0.0)  {
    }
  SpeedPack_(const ContainerAllocator& _alloc)
    : speed(0.0)
    , acc(0.0)
    , dec(0.0)  {
  (void)_alloc;
    }



   typedef float _speed_type;
  _speed_type speed;

   typedef float _acc_type;
  _acc_type acc;

   typedef float _dec_type;
  _dec_type dec;





  typedef boost::shared_ptr< ::ros_whill::SpeedPack_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::ros_whill::SpeedPack_<ContainerAllocator> const> ConstPtr;

}; // struct SpeedPack_

typedef ::ros_whill::SpeedPack_<std::allocator<void> > SpeedPack;

typedef boost::shared_ptr< ::ros_whill::SpeedPack > SpeedPackPtr;
typedef boost::shared_ptr< ::ros_whill::SpeedPack const> SpeedPackConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::ros_whill::SpeedPack_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::ros_whill::SpeedPack_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::ros_whill::SpeedPack_<ContainerAllocator1> & lhs, const ::ros_whill::SpeedPack_<ContainerAllocator2> & rhs)
{
  return lhs.speed == rhs.speed &&
    lhs.acc == rhs.acc &&
    lhs.dec == rhs.dec;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::ros_whill::SpeedPack_<ContainerAllocator1> & lhs, const ::ros_whill::SpeedPack_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace ros_whill

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::ros_whill::SpeedPack_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::ros_whill::SpeedPack_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ros_whill::SpeedPack_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ros_whill::SpeedPack_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ros_whill::SpeedPack_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ros_whill::SpeedPack_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::ros_whill::SpeedPack_<ContainerAllocator> >
{
  static const char* value()
  {
    return "0a1fd5b06ddb3a692b56f449ac43917c";
  }

  static const char* value(const ::ros_whill::SpeedPack_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x0a1fd5b06ddb3a69ULL;
  static const uint64_t static_value2 = 0x2b56f449ac43917cULL;
};

template<class ContainerAllocator>
struct DataType< ::ros_whill::SpeedPack_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ros_whill/SpeedPack";
  }

  static const char* value(const ::ros_whill::SpeedPack_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::ros_whill::SpeedPack_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float32 speed  # m/s   or rad/s\n"
"float32 acc    # m/ss  or rad/ss\n"
"float32 dec    # m/ss  or rad/ss\n"
;
  }

  static const char* value(const ::ros_whill::SpeedPack_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::ros_whill::SpeedPack_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.speed);
      stream.next(m.acc);
      stream.next(m.dec);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct SpeedPack_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::ros_whill::SpeedPack_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::ros_whill::SpeedPack_<ContainerAllocator>& v)
  {
    s << indent << "speed: ";
    Printer<float>::stream(s, indent + "  ", v.speed);
    s << indent << "acc: ";
    Printer<float>::stream(s, indent + "  ", v.acc);
    s << indent << "dec: ";
    Printer<float>::stream(s, indent + "  ", v.dec);
  }
};

} // namespace message_operations
} // namespace ros

#endif // ROS_WHILL_MESSAGE_SPEEDPACK_H