member_info = """
**__User Info__**
Name: {member}
ID: `{member.id}`
Creation Date: **{member.created_at}**
Mention: {member.mention}
**__Member Info__**
Display Name: {member.display_name}
Join Date: **{member.joined_at}**
Roles: {role_list}
"""

user_info = """
**__User Info__**
Name: {user}
ID: `{user.id}`
Creation Date: **{user.created_at}**
Mention: {user.mention}
"""

channel_info = """
**__Channel Info__**
Name: {channel}
ID: `{channel.id}`
Creation Date: **{channel.created_at}**
Mention: {channel.mention}
"""

role_info = """
**__Role Info__**
Name: {role}
ID: `{role.id}`
Creation Date: **{role.created_at}**
Mention: {role.mention}
Hoisted: {role.hoist}
Mentionable: {role.mentionable}
Integration: {role.managed}
Position: {role.position}
Colour: {rcolour}
Member Count: {rmcount}
"""