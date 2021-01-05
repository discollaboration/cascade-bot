from discord import Embed, Member, User, TextChannel, CategoryChannel, VoiceChannel, Role, Guild
from typing import Union
from datetime import datetime

from bot.bot import VER
from .templates import member_info, user_info, channel_info, role_info

def default_embed(title: str, description: str) -> Embed:
    e = Embed(title=title, colour=0x87CEEB, description=description)
    e.set_footer(text=f"Cascade@{VER}")
    e.timestamp = datetime.now()
    return e

def MemberInfo(member: Member) -> Embed:
    desc = member_info.format(member=member, role_list=', '.join([r.mention for r in member.roles]))
    e = default_embed(f"**Member: {member}**", desc)
    e.set_author(name=member.name, icon_url=str(member.avatar_url))
    return e

def UserInfo(user: User):
    desc = user_info.format(user=user)
    e = default_embed(f"**User: {user}**", desc)
    e.set_author(name=user.name, icon_url=str(user.avatar_url))
    return e

def ChannelInfo(channel: Union[TextChannel, VoiceChannel, CategoryChannel]):
    desc = channel_info.format(channel=channel)
    e = default_embed(f"**Channel: {channel}**", desc)
    return e

def RoleInfo(role: Role):
    desc = role_info.format(role=role, rcolour=hex(role.colour.value), rmcount=len(role.members))
    e = default_embed(f"**Role: {role}**", desc)
    return e

def GuildInfo():
    pass