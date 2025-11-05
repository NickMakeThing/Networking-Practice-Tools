#format is:   category = {answer: questions}
#should also print what category the question is from when asking - by printing the dict variable's name
#take dict key, make lowercase, get rid of spaces, and get rid of hyphen
#make user's answers lowercase, take out spaces, and get rid of hyphen before checking
#count right/wrong answers. put all wrong answers and their questions into a single dict that can be printed out at the end
#the user will be able to take that dict and quiz on those questions specifically afterward.


#wtf is a recursive static route? answer: https://youtu.be/rwkHfsWQwy8?si=WpbnCebGB2UVEIEJ&t=1645
#made the mistake of making a question that takes two answers at the same time. 
#i think it was the 'console buffer' one in syslog. i need to go back and fix it
#woah crazy trivia: cisco exports 'NPE'(no payload encryption) versions of IOS to countries that have restrictions on encryption technology.
#wait 'logging synchronous' is configured on console line and not as a (config)# command?

#missing: 802.11 frame types "Which 802.11 frame type is Association Response?"
#spine leaf architecture - btw how tf is it more scalable?
#tcp header
#wlc interfaces
#wildcard practice
#mac addresses
#can we configure portchannel int as trunk/access, etc while it's down? #look up port channel configuration best practice
#should experiment with making etherchannels, especially l3 ones. e.g., only configuring 'noswitchport' on the portchannel afterwards.
#commands:
    #dhcp show commands. show lease, show dhcp binding table
    #which cdp/lldp commands show OS, build model, serial number etc, or w/e
    #note: ocg and pt have inconsistency: show mac address-table VS show mac-address-table
    #what password encryption type does service password encryption make the plain text passwords?: 7 (vignere)
    #what password encryption type does enable secret make the entered password? 5 i think (md5)
    #what does enable secret 5 sdlgsdofsdkfj do
    #what is the number $1$ in this type of password form do (md5) 
    #effects of different types of ospf mismatches.
questions_dict = {
    'missed':{ #things i forgot to put in other sections
        frozenset({'show ip arp'}):['what command shows the arp-cache of a cisco device?'],
        frozenset({'show interfaces f0/1 switchport'}):['what command shows a large amount of information about f0/1? operational/admin\' trunking mode, access vlan, voice vlan, etc'],
        frozenset({'show mac address-table'}):['what command shows a switch\'s CAM table?'],
        frozenset({'show mac address-table dynamic'}):['what command will no longer list mac-addresses learned on port-security configured port?'],
    #   frozenset({'show mac address-table aging-time'}):[''],
    #   frozenset({'show mac address-table count'}):[''],
    #   frozenset({'show mac address-table static'}):[''],
        frozenset({'show mac address-table secure'}):['what commands will show table of learned addresses of port-security enabled ports?'],
        frozenset({'show mac address-table static'}):['what commands will show table of sticky-learned addresses?'],
        #after port-security is enabled, learned addresses learned AFTER will still show up in basic 'show mac ad' command, but NOT with the 'dynamic' arg/keyword
        frozenset({'stateless'}):['what kind of dhcp is used in combination with SLAAC to provide dhcp \'option\' information? e.g., dns server address'],
        frozenset({'discover', 'offer', 'request', 'acknowledge'}):['what are the types of messages sent between a DHCP server and it\'s client?'],
        frozenset({'solicit','advertise','request','reply'}):['what are the types of messages sent between a DHCPv6 server and it\'s client?'],
        frozenset({'router advertisement'}):['how do both stateless & stateful DHCPv6 clients learn their prefix length and default gw ip?']
    },
    'aireos':{
        frozenset({'advanced'}):['upon logging into a aireos WLC, what should be clicked on first in order to configure the device?'],
        frozenset({'interface'}):['what is configured first?'],
        frozenset({'controller','interface'}):['what things to click to begin configuring interface? separate two answers with comma'],
        frozenset({'name','vlan'}):['what first two things to configure on interface? separate with comma' ],
        frozenset({'ip address','gw address','dhcp address'}):['what other (after the first two) things to configure on interface'],
        frozenset({'WLAN'}):['what to configure after interface?'],
        frozenset({'profile name','ssid','wlan id'}):['what are first things to configure on wlan'],
        frozenset({'enable','radio policy','interface'}):['what is configured in the general tab'],
        frozenset({'wpa2','psk','aes'}):['what is configured in the security tab'],
        frozenset({'max clients','session timeout'}):['what is configured in the advanced tab'],
    },
    'low_layer':{
        frozenset({'show interfaces status'}):['command that shows each port\'s duplex, speed(s), access vlan, L1 connection status'], #doesnt work in PT
        frozenset({'show interfaces f0/1'}):['what command provides L1/L2 error counters for interface f0/1?'],
        #what command shows the stats below?
        frozenset({'64'}):['what is the default minimum frame size in bytes?'],
        frozenset({'1518'}):['what is the default maximum frame size in bytes?'],
        frozenset({'runts'}):['counts frames that are smaller than the minimum frame size?'],
        frozenset({'giants'}):['counts frames that are larger than the maximum frame size?'],
        frozenset({'CRC'}):['counts FCS comparison check failures'],
        frozenset({'frame'}):['counts frames that have an incorrect format'],
        frozenset({'input errors'}):['totals a number of other error counts (crc, no buffer, runts, giants, etc)'],
        frozenset({'output errors'}):['counts failures to transmit frames'],
        frozenset({'collisions'}):['counts collisions, which also result in other error counters going up. (two devices speak on half-duplex network simultaneously)'],
        frozenset({'late collisions'}):['counts collisions that happen after the 64th byte has been transmitted.'],
        frozenset({'duplex mismatch'}):['what is a common cause of the \'late collisions\' counter going up?'],
        #(runts, CRC, frame) can all be caused by collisions
        frozenset({'line/protocol'}):['what statuses does up/up tell us about? answer with the form: answer1/answer2'],
        #if 
        frozenset({'100mbps'}):['if one side of a link sends with 100mbps full duplex, but isn\'t negotiating, what SPEED does the negotiating side use?'],
        frozenset({'10mbps'}):['if one side of a link is not negotiating, AND the other side (10/100/1000) cannot sense the speed, what SPEED does the negotiating side use?'],
        frozenset({'half'}):['if one side of a link sends with 100mbps full duplex, but isn\'t negotiating, what DUPLEX does the negotiating side use?'],
        frozenset({'full'}):['if one side of a link sends with 1gbps full duplex, but isn\'t negotiating, what DUPLEX does the negotiating side use?'],
},
    'syslog':{ 
        #Every Awesome Cisco Engineer Will Need Icecream Daily (EACEWNID) neumonic for remembering severity names
        #should add some commands
        frozenset({'Every Awesome Cisco Engineer Will Need Icecream Daily'}):['what mnemonic helps remember the severity levels?'],
        frozenset({'5'}):['what is the severity in:\n21:48:21: %OSPF-5-ADJCHG: Process 1, Nbr 3.3.3.3 on GigabitEthernet0/1 from FULL to DOWN, Neighbor Down: Dead timer expired'],
        frozenset({'OSPF'}):['what is the facility in:\n21:48:21: %OSPF-5-ADJCHG: Process 1, Nbr 3.3.3.3 on GigabitEthernet0/1 from FULL to DOWN, Neighbor Down: Dead timer expired'],
        frozenset({'ADJCHG'}):['what is the mnemonic in:\n21:48:21: %OSPF-5-ADJCHG: Process 1, Nbr 3.3.3.3 on GigabitEthernet0/1 from FULL to DOWN, Neighbor Down: Dead timer expired'],
        frozenset({'console','buffer'}):['by default, which two places are syslog messages sent to? separate each with a comma'],
        frozenset({'disabled'}):['are syslog messages to vty lines enabled or disabled by default?'],
        frozenset({'emergency'}):[0],
        frozenset({'alert'}):[1],
        frozenset({'critical'}):[2],
        frozenset({'error'}):[3],
        frozenset({'warning'}):[4],
        frozenset({'notification'}):[5],
        frozenset({'informational'}):[6],
        frozenset({'debug'}):[7],
        frozenset({'show logging'}):['what command shows logs stored in the buffer?'],
        frozenset({'logging monitor','terminal monitor'}):['to enable log messages being sent to vty line users, what two commands must be entered? separate the commands with a comma'],
        frozenset({'0-4'}):['what range of syslog severity will be sent when setting the severity level to 4? answer with x-y'],
        frozenset({'logging host 1.2.3.4'}):['what command sends syslog messages to a syslog server with ip 1.2.3.4?'],
        frozenset({'logging trap 4'}):['what command sets the severity level of messages sent to syslog servers to 4?'],
        # frozenset({'debug'}):['what kind of logging output doesn\'t show severity levels?'],
        # frozenset({''}):[''],
        #debug command will output messages of specific 'facilities', e.g., ospf, etc
        #debug command output does not list severity level
        #does the 'debug' command print all messages under 7 like the 'logging' command would?

        #'terminal monitor' has to be done by the user during the vty session, and i think it has to be done every time

},

    'automation':{

        #'configuration drift'?

        #ansible
        frozenset({'ansible','puppet','chef'}):['name the three typical configuration management platforms'],
        frozenset({'ssh'}):['what does ansible use to automatically connect to devices, update configurations, get information, etc?'],
        frozenset({'ansible'}):['which configuration management platform(s) use a push model? (central service pushes configs to devices)'],
        frozenset({'puppet','chef'}):['which configuration management platform(s) use a pull model? (devices pull new configs from service)'],
        frozenset({'no'}):['do devices that are managed by ansible have agents running on them?'],
        frozenset({'playbook','yaml'}):['in ansible, what files contain logic and tasks/actions that should be carried out, and what language/format is it written in? separate answers with a comma'], #https://www.youtube.com/watch?v=AdQJY3cuqfI
        frozenset({'inventory'}):['what files list and define devices that ansible will manage?'],
        frozenset({'template','jinja2'}):['In ansible, what kind of file holds device configuration with variable names, and what language/format is it written in? separate answers with a comma'],
        frozenset({'variables','yaml'}):['In ansible, what files holds the values of the variables that are used, and what format/language is it written in? separate answers with a comma'],
        frozenset({'configuration management'}):['what term is used to describe what ansible does?'],

        #terraform
        frozenset({'provisioning'}):['what term is used to describe what terraform does?'], #or 'infrastructure provisioning'
        frozenset({'HCL'}):['what language are terraform configurations written in?'],
        # frozenset({''}):[''],
        # frozenset({''}):[''],
        
        #both
        frozenset({'terraform'}):['is ansible or terraform better for spinning up/tearing down virtual instances and infrastructure?'],
        frozenset({'ansible'}):['is ansible or terraform better for on-going management of existing or persistent infrastructure?'],


    },
    'DNS':{
        #theres also the ip domain list command, which i really doubt will be on the CCNA exam
        frozenset({'ip host example.com 1.2.3.4'}):['what command creates a dns entry to translate example.com to 1.2.3.4 for clients or commands?'],
        frozenset({'ip name-server 1.1.1.1'}):['what command sets 1.1.1.1 as a dns server address to query for itself or on behalf of DNS clients?'],
        frozenset({'ip dns server'}):['what command turns a device into a dns server?'],
        frozenset({'ip domain lookup'}):['what command should be entered to enable the use of a remote dns server when a dns entry isn\'t found locally?'],
        #this needs to be on if you want the router to do a recursive dns lookup for clients too. see ctrlf"the enterprise DNS acts as a recursive DNS server" in OCG
        frozenset({'nslookup youtube.com'}):['on most OS\'s, what command will do a DNS query for youtube.com?'],
        frozenset({'A'}):['what kind of DNS record gives an IPv4 address?'],
        frozenset({'AAAA'}):['what kind of DNS record gives an IPv6 address?'],
        #there are also CNAME records
    },
    'files':{
        #TFTP/FTP
        #IOS filesystem
        #it isn't clear whether i should walk into the exam thinking TFTP is 'unreliable' or has inferior reliability. jeremy IT Labs mentions TFTP's 'lock-step communication'.
        # not clear if i should walk in remembering things about SCP & SFTP
        #ftp
        frozenset({'active'}):['what form of FTP has the server initiate the Data connection?'],
        frozenset({'passive'}):['what form of FTP has the client initiate the data connection? e.g., if the client is behind a firewall.'], 
        frozenset({'ip ftp username'}):['what command sets the ftp username?'],
        frozenset({'ip ftp password'}):['what command sets the ftp password?'],
        frozenset({'copy ftp: flash:'}):['what command begins the prompts to download a file to flash storage?'],
        frozenset({'boot system flash:imagename.bin'}):['once a new IOS image has been downloaded as imagename.bin into flash, what command configures the device to use it?'],
        frozenset({'write memory'}):['what command should be used to ensure the \'boot system\' command is saved and takes effect after reload?']
},

    'ospf':{
        frozenset({'RID','subnet','cost'}):['an LSA contains what information? separate each with a comma.'],
        #also contains portstate^ (up/up)
        frozenset({'LSAs'}):['what are LSDBs made up of?'],
        frozenset({'0'}):['which area is the backbone?','which area should be used in single area ospf?'],
        frozenset({'drother','DR','bdr'}):['for ospf routers that share a single subnet, what are the different roles they take on? ? separate each with a comma.'],
        frozenset({'router ospf 1'}):['what command enters ospf config mode for process 1?'],
        frozenset({'network 1.2.3.0 0.0.0.3 area 0'}):['what command advertises 1.2.3.0/30 and sends ospf hellos from interfaces in that subnet? (area 0)'],
        frozenset({'ip ospf 1 area 0'}):['what interface command advertises the subnet on that interface and sends hellos from it? (process 1, area 0)'],
        frozenset({'internal'}):['what do we call a router that has all its interfaces in the same area?'],
        #ABRs have separate LSDBs per area they're in
        frozenset({'ABR'}):['what do we call routers that have interfaces in more than one area?'],
        frozenset({'backbone'}):['what do we call routers connected to area 0? ___ routers'],
        frozenset({'intra-area'}):['what kind of route is to a destination within the same area?'],
        frozenset({'inter-area'}):['what kind of route is to a destination within a different area?'],
        frozenset({'passive-interface g0/2'}):['what command is used in ospf config mode to make g0/2 a passive interface?'],
        frozenset({'passive-interface default'}):['what command in ospf config mode makes all ospf interfaces passive'],
        frozenset({'no passive-interface g0/0'}):['after making all interfaces ospf-passive by default, what ospf mode command makes specific interfaces not passive? enter the command for g0/0'],
        frozenset({'default-information originate'}):['what command is used in ospf config mode to advertise an existing default route?'],
        frozenset({'clear ip ospf process'}):['what command is used after setting a new router ID to start using it?'],
        frozenset({'ASBR'}):['what kind of ospf router does a router become after the \'default-information originate\' is entered?'],
        #{'router id','loopback','interface'}:['list the three things that are used to select a router ID.'],
        #router id selection order. i think its: #manually set RID -> highest lo address -> highest interface address 
        #br,bdr election
        #p2p network details
        #equal cost load balancing
        #cost
        frozenset({'100'}):['what is ospf\'s default reference bandwidth? just enter the number, and not its type of rate'],
        frozenset({'mbps'}):['what type of rate is ospf\'s reference bandwidth in? (kbps/mbps/gbps)'],
        frozenset({'referencebw/intspeed'}):['using variables referencebw and intspeed, enter the formula that gives ospf cost.'],
        frozenset({'10'}):['what is the default ospf cost of a 10mbps link?'],
        frozenset({'1'}):['what is the default ospf cost of a 100mbps link?'],
        frozenset({'1'}):['what is the default ospf cost of a 1gbps link?'],
        frozenset({'auto-cost reference-bandwidth 1000'}):['what ospf mode command changes the refence bandwidth to 1gbps?'],
        frozenset({'show ip ospf interface g0/1'}):['what command will show the ospf cost of g0/1, among other information about it?'],
        frozenset({'10'}):['if the reference bandwidth is 100,000 what will be the cost of a 10gbps interface'],
        frozenset({'ip ospf cost 5'}):['what interface command manually sets the ospf cost of that interface to 5?'],
        frozenset({'outgoing'}):['does ospf use the cost of the nexthop, or the outgoing interface when calculating total cost of a route? (outgoing/nexthop)'],
        frozenset({'bandwidth 50000'}):['what interface command labels the interface with a bandwidth of 50 mbps, which effects ospf cost calculation and not the actual bandwidth?'],
        frozenset({'show ip ospf interface brief'}):['what command lists ospf information in a brief format of each interface: cost, dr/bdr/drother, neighbor count, area'],
        #neighbors
        frozenset({'down','init','2way'}):['what neighbor states do devices go through to get to become basic neighbors? (not \'neighbor adjacencies\')'],
        frozenset({'exstart','exchange','loading','full'}):['what neighbor states do devices go through to exchange LSDB information and become a full adjacency? separate each with a comma'],
        frozenset({'down'}):['what neighbor state is an interface in if it has sent a hello with its own RID, but not yet informed of the other device\'s RID?'],
        frozenset({'init'}):['what neighbor state is an interface in if it has received a hello with the RID of the other, but not it\'s own?'],
        frozenset({'2way'}):['what neighbor state is an interface in if it has received a hello with both it\'s own RID & the RID of the other side?','which neighbor state do DR/BDR elections take place?'],
        frozenset({'exstart'}):['which neighbor state has a \'master\'-\'slave\' election by exchanging \'DBD\' packets and comparing RIDs?'],
        frozenset({'exchange'}):['what neighbor state involves an exchange of DBDs that summarize information? (so neighbors can check if their LSDBs contain that information)'],
        frozenset({'loading'}):['what neighbor state involves sending LSRs/LSUs/LSAcks (requests/updates/acknowledgments) to sync their LSDBs? '],
        frozenset({'full'}):['what neighbor state is signifies a full \'neighborship adjacency\' and synced LSDBs?'],
        frozenset({'10'}):['what is the default hello interval?'],
        frozenset({'40'}):['how many seconds is the default dead timer?'],
        frozenset({'ip ospf hello-interval 5'}):['what command changes an interface\'s ospf hello interval to 5 seconds?'],
        #shows information about the NEIGHBOR not the local device. for similar brief information on local device use 'show ip ospf interface brief' instead 
        frozenset({'show ip ospf neighbor'}):['what command will show information of ospf neighbors in a brief format? (neighbor\'s id, neighbor state, dr/bdr/other)'],
        #DR/BDR elections
        #highest interface priority -> highest router ID
        frozenset({'ip ospf priority 69'}):['what interface command changes ospf priority to 69 to influence a DR/BDR election?'],
        frozenset({'higher'}):['is it higher or lower priorities that win OSPF DR elections?'],
        frozenset({'router ID'}):['what wins a DR/BDR election if all devices have the same priority?'],
        frozenset({'no'}):['is there a feature for devices to \'preempt\' in DR/BDR hierarchies? answer yes/no'],
        frozenset({'DRother'}):['if a device with the highest OSPF priority comes up after a DR election has taken place, will it become DR,BDR, or DRother?'],
        frozenset({'BDR'}):['if a device has the highest ospf priority, but is DRother. What role will it have after the DR goes down?'], 
        frozenset({'2way'}):['what neighbor state do DRothers share with each other?'],
        frozenset({'Full'}):['what neighbor state do DRothers share with DRs/BDRs?'],
        #network types
        frozenset({'broadcast'}):['on what network type will DR/BDR elections occur?'],
        frozenset({'point-to-point'}):['on what network type will DR/BDR elections NOT occur?'],
        frozenset({'ip ospf network point-to-point'}):['what interface command changes the network type to point-to-point?'],
        frozenset({'30'}):['how many mins is the \'max age\' timer of each individual LSA (before it gets flooded again)'],
        #neighbor troubleshooting # --------------------- should also chekc phnum.txt for troubleshooting things not mentioned in jeremyslabs
        #neighbors must be: same(subnet, area, hello/dead timers, MTU settings, network type) & unique RIDs
        #   in MTU mismatch, ospf state will flap between DOWN and EXSTART
        #   in network type mismatch, ospf state will be FULL, but wont work properly
        #ospf process (router ospf 1) must not be shutdown
        frozenset({'show ip protocols'}):['what command can be used to view ospf information when stuck in user mode?'],
        frozenset({'mtu','subnet','area','timers','network type'}):['list all kinds of neighbor mismatches, separated by a comma.'],
        frozenset({'network type'}):['what type of ospf neighbor mismatch will show as \'full\', but result in ospf routes not being learned?'],
        frozenset({'router id'}):['what ospf detail will cause neighbor formation to fail when not unique on each device?'],
        frozenset({'interface'}):['if ospf network and interface commands (to advertise a subnet) are configured and conflict with each other, (e.g. they use different area IDs) which will take override the other? answer \'interface\' or \'network\''],
        frozenset({'0'}):['on a \'broadcast\' network, there should be at least one router that doesnt have a priority of - what?'],
        #how to display hello/dead intervals?
        #LSA types 
        frozenset({'type 1'}):['which type of LSA lists details of an individual router? (RID, neighbors, interfaces/their state, ip address/masks)'],
        frozenset({'type 2'}):['which type of LSA is only generated by DRs of broadcast networks that have more than 2 routers?'],
        frozenset({'type 3'}):['which type of LSA is generated by ABRs and provides a summary information to another OSPF area?'],
            #i think type 3s do not necessarily send route summaries #https://learningnetwork.cisco.com/s/question/0D53i00000Kt7fvCAB/ospf-summarylsa-type-3 #https://networklessons.com/ospf/ospf-lsa-types-explained
        frozenset({'type 5'}):['what type of LSA is generated by ASBRs to describe routes outside of the OSPF domain? (AKA AS)'], #jeremy IT labs mentions type 5 instead of type 3, and OCG does the opposite
        #show ip ospf database [summary]
},
    'etherchannel':{
        #show commands & legend
        #
        frozenset({'3'}):['what will be the 1998 stp cost of a LAG that provides 2 to 8 gbps total?'],
        #the long cost of an 2 to 8 gbps would be something like 20,000,000,000/(gbps * 1000*1000) since calculation is done in kbps
        frozenset({'show etherchannel summary'}):['what command shows information about port channels?'],
        frozenset({'P'}):['what etherchannel summary letter means the portchannel is bundled and working'],
        frozenset({'U'}):['what etherchannel summary letter means the portchannel is in use and working'],
        frozenset({'D'}):['what etherchannel summary letter means the portchannel is down?'],
        frozenset({'S'}):['what etherchannel summary letter means the portchannel is a layer 2 channel?'],
        frozenset({'R'}):['what etherchannel summary letter means the portchannel is a layer 3 channel?'],
        frozenset({'show etherchannel port-channel'}):['what other show command shows brief information about port channels?'],
        frozenset({'suspended'}):['what does lowercase \'s\' mean in etherchannel summary?','Besides \'D\'/\'Down\', what etherchannel status suggests a link is not functioning? enter the unabbreviated status term.'],
        frozenset({'port-channel load-balance src-mac'}):['what command sets the portchannel to load balance based off the src mac?'],
        frozenset({'port-channel load-balance src-dst-port'}):['what command sets the portchannel to load balance based off both the src & dst ports?'],
        frozenset({'lacp','pagp','etherchannel'}):['what are the 3 etherchannel protocols/options? separate each with commas'],
        frozenset({'channel-group 69 mode on'}):['what command configures a range of interfaces to become an etherchannel LAG as channel-group 69?'],
        frozenset({'channel-group 70 mode active'}):['what command configures a range of interfaces to initiate LACP as channel-group 70?'],
        frozenset({'channel-group 70 mode passive'}):['what command configures a range of interfaces to listen for LACP initiation as channel-group 70?'],
        frozenset({'channel-group 71 mode desirable'}):['what command configures a range of interfaces to initiate PAgP as channel-group 71?'],
        frozenset({'channel-group 71 mode auto'}):['what command configures a range of interfaces to listen for PAgP initiation as channel-group 71?'],
        frozenset({'no switchport'}):['what interface command on a portchannel turns it into a L3 portchannel?'],
        #can we configure portchannel int as trunk/access, etc while it's down?
},
    'ssh':{
        frozenset({'ip domain-name example.com'}):['what command sets the domain name example.com? (to later generate a key)'],
        frozenset({'hostname R1'}):['what command sets the host name R1? (to later generate a key)'],
        frozenset({'crypto key generate rsa modulus 1024'}):['what command generates an rsa key with modulus length of 1024?'],
        frozenset({'ip ssh version 2'}):['what command sets ssh to version 2?'],
        frozenset({'768'}):['what is the minimum modulus length to configure ssh version 2?'],
        frozenset({'line vty 0 4'}):['what command enables configuration for 5 concurrent ssh users? specifically the first 5 channels?'],
        frozenset({'transport input ssh'}):['what command enables ssh on vty lines?'],
        frozenset({'access-class 1 in'}):['what command uses access list 1 to control who can use the vty lines?'],
        #doesn't have 'ip' at the start, unlike 'ip access-group [acl] in'
        frozenset({'standard'}):['what type of access list is typically applied to vty lines?'],
        #should make question addressing can't use 'login' configuration for ssh, only 'login local' and some other stuff works
        frozenset({'login local'}):['what command enables authentication on vty lines that uses locally defined usernames/passwords?'],
        #not sure if its exec timeout or session timeout that resets its timer when users do something
        frozenset({'exec-timeout 5 30'}):['what command configures the vty line to automatically close after 5 minutes and 30 seconds of the user not doing anything?'],
        frozenset({'username bob password toast69'}):['what command creates a username \'bob\' with password \'toast69\'?'],
        frozenset({'transport input none'}):['what command disables vty lines?'],
        frozenset({'transport input all'}):['what command enables both telnet and ssh'],
        frozenset({'telnet'}):['which \'transport input\' method is enabled by default on catalyst switches?'],
        frozenset({'ip default-gateway 1.2.3.4'}):['a switch is on a lan that has a default gateway 1.2.3.4. what command is entered to ensure that the switch can respond & connect to ssh clients outside of the switch\'s lan?'],
        frozenset({'svi'}):['what should be configured on a switch to give it an ip address so clients may ssh into it?']
    #ssh bob@1.2.3.4    #ssh -l bob 1.2.3.4
},
    'vlans':{
            #TODO below
        # """
        # checkout incase missed anything:
        # different routing capabilities vary between L3 switch models .
        #         ocg recommends viewing https://www.cisco.com/go/cfn to see differences
        # """
        #trunk security best practices? disable vlan 1, make native random unused vlan,
        #DTP apparently no longer in the exam
        # {'access'}:['what does the link become when DTP configurations are auto+auto?'],
        # {'access'}:['what does the link become when DTP configurations are auto+access?'],
        # {'access'}:['what does the link become when DTP configurations are desirable+access?'],
        # {'trunk'}:['what does the link become when DTP configurations are auto+desirable?'],
        # {'trunk'}:['what does the link become when DTP configurations are trunk+auto?'],
        # {'trunk'}:['what does the link become when DTP configurations are desirable+desirable?'],

        #trunk configuration
        #vlan ranges
        frozenset({'1-1005'}):['what is the \'normal\' vlan range?'],
        frozenset({'1006-4094'}):['what is the \'extended\' vlan range?'],

        #show commands and troubleshooting
        # 'show interfaces trunk'
        # {'show vlan brief'}:[''], #barely any difference between this and show vlan
        frozenset({'show vlan id 69'}):['what command shows what ports are assigned to specifically vlan 69?'],
        frozenset({'show vlan'}):['what command shows each vlan and which ports are assigned to them?'],
        # {'allowed list'}:['the \'vlans allowed\' section of the \'show interfaces trunk\' command refers to vlans that are in the ... '],
        frozenset({'exist','not shut'}):['the \'vlans allowed and active in management domain\' section of the \'show interfaces trunk\' command refers to vlans that are in the allow list that are ... 2 things. separate answers with comma.'],
        frozenset({'show interfaces trunk'}):['what command shows each trunk\'s allow list and native vlan?'],
        frozenset({'show interfaces g0/0 trunk'}):['what command shows the allow list and native vlan on g0/0\'s trunk?'],
        frozenset({'show interfaces g0/1 switchport'}):['what command shows various L2 configuration information of g0/1? (admin/operational port mode, vlan, voice vlan, etc)'],
        frozenset({'show vtp status'}):['what command shows vtp information'],
        #configuration
        frozenset({'switchport mode access'}):['what command configures the port to only be an access port?'],
        frozenset({'switchport access vlan 69'}):['what command sets the access port\'s vlan to 69?'],
        frozenset({'switchport voice vlan 70'}):['what command sets the voice vlan of a port to vlan 70?'],
        frozenset({'switchport trunk encapsulation dot1q'}):['what command sets the trunking protocol to dot1q?'],
        frozenset({'switchport mode dynamic desirable'}):['what command configures a port to initiate DTP messages to try and form a trunk?'],
        frozenset({'switchport trunk allowed 10,20,30'}):['what command allows vlans 10,20, and 30 onto the trunk?'],
        #^this question has some odd bug, where the correct answer doesn't register as correct
        # {'switchport trunk allowed add 40'}:['what command adds vlan 40 to a trunk\'s already existing allow list?'],
        # {'switchport trunk allowed remove 40'}:['what command removes vlan 40 from a trunk\'s allow list?'],
        frozenset({'switchport trunk allowed 3-7'}):['what command allows all vlans between 3 and 7 onto the trunk?'],
        frozenset({'switchport nonegotiate'}):['what command stops a port from partaking in DTP completely, such that it does not even send/process DTP frames?'],
        frozenset({'switchport trunk native 123'}):['what command sets the trunk\'s native vlan to 123?'],
        frozenset({'no'}):['should the native vlan be included in the \'allowed vlan\' command? (yes/no)'],
        #difference between this^ and just setting as trunk/access?
        #vlan names
        frozenset({'VLAN0069'}):['what is the default name for vlan 69 after creation?'],
        frozenset({'name HORSE'}):['after entering vlan config mode, what command changes the name to \'HORSE\'?'],
        #ip phones

        #ROAS
        # {'ports'}:['beside \'no shut\' what does an SVI need to be UP/UP?'],
        # {'vlan'}:['what other mode should be entered and\'no shut\' to bring up an SVI beside the vlan INTERFACE?'],
        #for an SVI to be up/up: vlan needs to exist, 1 port in vlan, vlan interface 'no shut'ed
            #unsure: 'no shut' in basic vlan mode.
            #is autostate default?
        frozenset({'autostate'}):['what feature determines these requirements for an SVI to be up/up? [vlan exists, 1 port in vlan, vlan interface \'no shut\']'],
        frozenset({'trunk'}):['what kind of DTP setting should be set to both sides of a ROAS link?'],
        frozenset({'no'}):['is an IP required on the physical/parent port of ROAS subinterfaces?'],
        frozenset({'sub interface','physical port'}):['what are two ways to handle native vlan on the router\' end of a ROAS link? separate answers with a comma'],
        frozenset({'encapsulation dot1q native'}):['what command is used to configure native vlan on a sub interface?'],
        frozenset({'ip address'}):['what needs to be configured on the physical interface so it\'s used for the native vlan?'],
        #^need to revise how each of these two are configured
        frozenset({'int g0/0.10'}):['what command is used to enter interface command mode sub interface on g0/0 that is suitable for vlan 10?'],
        frozenset({'encapsulation dot1q 10'}):['what sub-interface command sets the vlan of the frames it should handle to vlan 10?'],
        frozenset({'ip address 1.2.3.1 255.255.255.0'}):['what command sets an ip address on the sub-interface to 1.2.3.1/24?'],
        frozenset({'show vlans'}):['what command on a router can verify the use/existance of vlans of sub-interfaces?'],
        frozenset({'show ip int brief'}):['what command can be used to see the up/up state of an SVI?'],
        #Inter-VLAN with SVI
        frozenset({'ip routing'}):['what command is required on a L3 switch for intervlan routing to work?'],
        # {'sdm prefer'}:['what extra command is required by older switches for inter-vlan routing to work?']
        #probs not on exam^
        frozenset({'default route', 'routing protocol'}):['for SVI inter-vlan routing, either of what two things should be configured so clients can talk to other networks? (e.g., between buildings, over WANs). separate answers with comma.'],
        frozenset({'yes'}):['should there be an SVI for each VLAN when doing SVI-based intervlan routing? (yes/no)'],
        #L3 switchport
        frozenset({'no switchport'}):['what command is used on an interface to turn it into a routed port?'],
        #router switchport module
        frozenset({'SVI'}):['what is created/used to configure intervlan routing on a switchport module of a router?']
},
    'ACLs':{
        frozenset({'1-99','1300-1999'}):['what ranges are standard ACLs? separate ranges with a comma'],
        frozenset({'100-199','2000-2699'}):['what ranges are extended ACLs? separate ranges with a comma'],
        #configuration
        frozenset({'deny any'}):['what is implicitly at the end of every acl?'],
        frozenset({'permit any'}):['what can be put at the end of an ACL to turn it from a whitelist into a blacklist?'],
        # {'remark'}:['in place of \'permit\' or \'deny\', what key word can be used to leave a comment in an ACL?'],
        frozenset({'access-list 1 permit 0.0.0.0 255.255.255.255'}):['what is a longer way of writing out a \'permit any\' ACE as part of standard ACL 1?'],
        frozenset({'access-list 1 deny 1.2.96.0 0.0.7.255'}):['write a standard ACE for ACL 1 to deny packets from 1.2.96.0/21'],
        frozenset({'ip access-list standard dogfood'}):['what command enters ACL config mode for a standard ACL named dogfood?'],
        #intervals change on reload but maintain order of ACEs. 
        #theres also a 'resequence' command that replaces the current intervals of an ACL
        frozenset({'5 permit any'}):['what command in standard named ACL mode adds a \'permit any\' ACE with seq number 5?'],
        frozenset({'permit host 1.2.3.4'}):['what command in standard named ACL mode adds an ACE at the end of the ACL that allows anything from 1.2.3.4?'],
        frozenset({'access-class 5 in'}):['what command applies ACL 5 to vty clients in \'line vty\' mode?'],
        frozenset({'ip access-group 5 in'}):['what interface command applies ACL 5 to incoming traffic?'],
        frozenset({'10'}):['what is the default interval of each sequence number, if the seq number isn\'t explicitly entered?'],
        frozenset({'no 30'}):['in named ACL mode, what command deletes an ACE that has seq number 30?'],
        frozenset({'deny icmp any any'}):['in extended named ACL mode, write an ACE that denies all ping packets'],
        frozenset({'access-list 104 deny ip host 192.168.1.69 172.168.3.64 0.0.0.63'}):['write an ACE that denies traffic from 192.168.1.69 to 172.168.3.64/26 for numbered ACL 104. \ndon\'t use a wc for the source address.'],
        #tcp/udp gt,lt,list,range,eq & src port, dst ports
        frozenset({'permit tcp host 1.2.3.4 eq 69 host 69.69.69.69 range 80 100'}):['in extended named ACL mode, write an ACE that permits traffic from tcp port 69 of 1.2.3.4 to all ports 80 to 100 of 69.69.69.69. \ndon\'t use wc masks.'],
        frozenset({'deny udp 192.168.1.0 0.0.0.255 172.168.1.0 0.0.0.127 lt 80'}):['in extended named ACL mode, write an ACE that denies traffic from 192.168.1.0/24 to udp ports less than 80 of 172.168.1.0/25'],
        frozenset({'access-list 104 permit tcp 1.2.3.4 0.0.0.0 gt 69 any'}):['write an ACE that permits traffic from tcp ports above 69 of 1.2.3.4 to any IP address as part of a  numbered ACL 104. \nuse a wc for the source address.'],
        #/32 ACEs
        frozenset({'host'}):['what key word can precede an IP address in an ACE to match it as a /32 address?'],
        frozenset({'0.0.0.0'}):['what wildcard mask can be used to match a /32 address?'],
        frozenset({'ACL'}):['a numbered ACL has ace:\'access-list 1 deny 192.168.1.1\' what would entering this as a command with \'no\' prepended to it do? delete the ACE or entire ACL? \nanswer with either: ACE or ACL'],
        frozenset({'32'}):['what prefix length will the device think an address in a standard ACL is if it\'s wc mask is left out?'],
        #types
        frozenset({'standard'}):[
            'what type of ACL is typically used for VTY lines?',
            'what type of ACL is placed closest to a packet\'s destination?',
            ],
        frozenset({'extended'}):[
            'what type of ACL is placed closest to a packet\'s source?',
            ],
        #the ACEs/seq will be displayed out of order with this command, but you the displayed seq number help understand their order 
        frozenset({'show access-lists'}):['what command shows information about each ACL, It\'s type, and each ACE/seq number? '],
        #notable cases, e.g., allowing ospf, dhcp and ip helper
        frozenset({'generated'}):['what kind of packets are not filtered by outbound ACLs?'],
        # frozenset({'inbound'}):['which way should an ACL be placed to allow OSPF to operate'], #wtf did i mean by this
        frozenset({'permit ospf any any'}):['write a named-acl ACE that allows for OSPF to operate'],
        frozenset({'68/67'}):['what is the src/dst port of a dhcp request coming from a dhcp client to a relay agent/gateway? give numbers in this form: src/dst'],
        frozenset({'67/67'}):['what is the src/dst port of a dhcp request coming from a dhcp relay to a dhcp server? give numbers in this form: src/dst'],
},
    'stp':{
        #states
        frozenset({'listening','learning','forwarding','blocking','disabled'}):['what are the classic STP port STATEs? separate answers with comma.'],
        frozenset({'listening'}):['what classic STP state accepts bpdus, doesn\'t send them, and times out mac addresses?'],
        frozenset({'learning'}):['what classic STP state accepts/sends bpdus, & learns mac addresses?'],
        frozenset({'discarding','learning','forwarding'}):['what are the RSTP port STATEs? separate answers with comma.'],
        #timers 
        frozenset({'forwarding delay timer'}):['what determines how long each of the listening and learning states are?'],
        frozenset({'15'}):['how many seconds is the forward delay timer by default?'],
        frozenset({'2'}):['how many seconds is the hello timer by default?'],
        frozenset({'20'}):['in classic STP, how many seconds is the max age timer by default?'],
        frozenset({'6'}):['in RSTP, how many seconds is the max age timer by default?'],
        #bridge ID & classic port roles
        frozenset({'bridge id'}):['what is used to determine which switch becomes the root bridge?','if both switches on a link/segment have equal root cost, then lowest -what- decides which gets to make their port \'designated\'?'],
        frozenset({'priority','mac address'}):['what sections make up a BID? separate section names with a comma.'],
        frozenset({'32768'}):['what is the default bridge priority'],
        frozenset({'lowest'}):['does the highest or lowest bridge ID result in becoming the root bridge?'],
        frozenset({'designated'}):['what port role do all ports become on the root bridge?','what port role is on the other end of a root port?'],
        frozenset({'root cost'}):['lower -what- decides which switch on a link gets to make their port \'designated\'?'],
        frozenset({'root'}):['which ports point up-stream to the root bridge?','port with the lowest \'root cost\' takes on which role?'],
        frozenset({'16'}):['how many bits total is the \'bridge priority\' field of the bridge ID?'],
        frozenset({'4'}):['how many bits of the \'bridge priority\' field is actually used for priority values for PVST?'],
        frozenset({'12'}):['how many bits of the \'bridge priority\' field does the \'extended system ID\' (VLAD ID) part take up?'],
        frozenset({'4096'}):['by what interval does the bridge priority (actual priority field) increment/decrement?'],
        frozenset({'8196'}):['in pvst what is the total \'bridge priority\' if the priority is set to \' 8192 & the vlan is set to 4'],
        #selecting root port: path cost -> neighbors mac address -> port number 
        frozenset({'neighbor bridge id'}):['if multiple ports on a switch have the same root cost, then the lower -what- determines the root port?'],
        frozenset({'neighbor port id'}):['if multiple ports on a switch have the same root cost, and are connected to the same neighboring switch, then the lower -what- determines the root port?'],
        #RSTP port roles
        frozenset({'alternate'}):['what RSTP port role remains in discarding state, and prepares to immediately take over as a root port?'],
        frozenset({'backup'}):['what RSTP port role remains in discarding state, and prepares to immediately take over as a designated port. it\'s typically only used in hub topologies.'],
        #RSTP link types
        frozenset({'edge'}):['what RSTP link type connects to an end device and behaves like portfast?'],
        frozenset({'point-to-point'}):['what RSTP link type connects to another switch?'], 
        frozenset({'shared'}):['what RSTP link type connects to a hub?'],
        #cost

        #cost upstream switch sends its path cost to root down to the next downstream switch
        #the next downstream switch adds the cost of the interface receiving this message, and passes it on
        #process repeats and cost of each ingress port is accumulated down the path
        #this makes sense in classic STP, but what about RSTP where BPDUs are sent both ways?  

        frozenset({'designated'}):['in classic STP, which is the only type of port that BPDUs are sent out of'],

        #i think in classic STP every switch just forwards the root bridge's bpdus after convering
        #in rstp etc:

        #optional features
        frozenset({'portfast'}):['what optional feature skips listening and learning states, and is placed on edge ports (to endpoints)?','what feature makes a port an \'edge port\' in RSTP?'],
        frozenset({'trunk'}):['on what kind of ports will portfast not work on?'],
        frozenset({'bpdu guard'}):['what feature will put ports into err-disabled state on receiving a bpdu?'],
        frozenset({'bpdu filter','interface'}):['what feature prevents sending and receiving bpdus, effectively disabling stp on a port, and is it configured *globally* or on an *interface*? separate answers with a comma.'],
        frozenset({'bpdu filter','globally'}):['what feature will merely disable portfast and resume stp, and is it configured *globally* or on an *interface*? separate answers with a comma.'],
        frozenset({'rootguard'}):['what feature disables interfaces on receiving bpdus superior to the current root?'],
            #my notes, & possibly the OCG, say that rootguard auto-recovers disabled ports by default?
            #apparently it doesnt put them into 'errdisabled' it puts them into 'broken' or 'root-inconsistent' state
        frozenset({'loopguard'}):['what feature prevents ports from becoming designated ports, disabling them instead?'], #e.g., if something happens to a wire one way so that a port stops receiving bpdus
        #root/loop guard put ports in [root/loop]-inconsistent state
        # {'root-inconsistent'}:['what kind of port state does rootguard put ports into as a result of a violation?'],
},
    'stp_cost':{
        frozenset({'20000000'}):['what number is divided by n*mbps to get the corresponding *2004* STP cost?'],
        frozenset({'20000'}):['what number is divided by n*gbps to get the corresponding *2004* STP cost?'],
        frozenset({'100'}):['what is the *1998* STP cost for 10 mbps'],
        frozenset({'19'}):['what is the *1998* STP cost for 100 mbps'],
        frozenset({'4'}):['what is the *1998* STP cost for 1 gbps'],
        frozenset({'3'}):['what is the *1998* STP cost for n*1 gbps'],
        frozenset({'2'}):['what is the *1998* STP cost for 10 gbps'],
        frozenset({'2000000'}):['what is the *2004* STP cost for 10 mbps'],
        frozenset({'200000'}):['what is the *2004* STP cost for 100 mbps'],
        frozenset({'20000'}):['what is the *2004* STP cost for 1 gbps'],
        #according to these cisco docs, n*gbps for 2004 uses the formula, unlike the static values in 1998 see:
        #https://www.cisco.com/c/en/us/support/docs/switches/catalyst-6500-series-switches/24330-185.html ctrlf"Spanning Tree Port Cost Calculation"
        #non official sources will say 2gbps -> 10k cost, which is accurate, but also say 3gbps 10k cost, which is a misunderstanding (assuming the same 1998 logic applies to 2004)
        frozenset({'2000'}):['what is the 2004 STP cost for 10 gbps'],
        frozenset({'200'}):['what is the 2004 STP cost for 100gbps'],
        frozenset({'spanning-tree pathcost method long'}):['what command configures stp to use new cost numbers (2004)?'],
    },
    'stp_commands':{
        #interface commands
        #spanning-tree link-type [point-to-point/shared]. cbf remembering this one, & probably wont be on exam
        frozenset({'spanning-tree portfast'}):['what interface command configures portfast on that interface?'],
        frozenset({'spanning-tree bpduguard enable'}):['what interface command enables bpduguard on that interface?'],
        frozenset({'spanning-tree bpdufilter enable'}):['what interface command effectively disables STP on that interface?'],
        frozenset({'spanning-tree guard root'}):['what interface command enables rootguard on that interface?'],
        frozenset({'spanning-tree guard loop'}):['what interface command enables loopguard on that interface?'],
        frozenset({'spanning-tree vlan 5 cost 69'}):['what interface command will set the stp cost to 69 for vlan 5?'],
        frozenset({'spanning-tree vlan 5 port-priority 69'}):['what interface command will influence port role elections by forcing a \'port priority\' number to be 69 on vlan 5? (port priority represents port id of neighboring interface)'],
        #port cost, port priority(int number )
        #global
        frozenset({'spanning-tree portfast default'}):['what global config command will apply portfast to every access port?'],
        frozenset({'spanning-tree portfast bpduguard default'}):['what global config command will apply bpduguard on all portfast-enabled ports?'],
        frozenset({'spanning-tree loopguard default'}):['what global config command enables loopguard globally? (supposedly doesn\'t apply to designated ports)'],
        frozenset({'spanning-tree vlan 69 root primary'}):['what command sets a switch\'s STP priority to 4096 less than the current root\'s priority on vlan 69?' ],
        frozenset({'24576'}):['assuming all switch\'s on an STP network have default configuration, what priority does the \'... root primary\' set?'],
        frozenset({'spanning-tree vlan 69 root secondary'}):['what command will ALWAYS set a switch\'s STP priority to 28672 on vlan 69?'],
        frozenset({'spanning-tree vlan 69 priority 20480'}):['what command will explicitly set a switch\'s STP priority to 20480 on vlan 69?']
    },
    'ieee_standards':{ 
        frozenset({"802.3"}):['ethernet'],
        frozenset({"802.1x"}):['EAPoL','port-based authentication'],
        frozenset({"802.1q"}):['dot1q','vlan tags','trunking'],
        frozenset({"802.1D"}):['classic STP', 'common Spanning Tree'],
        frozenset({"802.1w"}):['RSTP'],
        frozenset({"802.1s"}):['MSTP'],
        frozenset({"802.11i"}):["WPA2"],
        frozenset({"802.3ad"}):['LACP'],
        frozenset({"802.11r"}):['roaming and "Fast transition (FT)"'],
        frozenset({"802.11"}):['wifi','2.4ghz, up to 2mbps'],
        frozenset({"802.11b"}):['2.4ghz, 11mbps'],
        frozenset({"802.11g"}):['2.4ghz, 54mbps'],
        frozenset({"802.11a"}):['5ghz, 54mbps'],
        frozenset({"802.11n"}):['2.4ghz & 5ghz, 600mbps'],
        frozenset({"802.11ac"}):['5ghz, 6.93gbps'],
        frozenset({"802.11ax"}):['2.4ghz & 5ghz & 6ghz, ~27.72Gbps'],
    },
    'qos':{
        #interesting related concept not on ccna tcp global synchronization: https://www.youtube.com/watch?v=bO5mQ1EJ0rg
        #https://www.youtube.com/watch?v=UE-pZsD77Wo
        #https://www.youtube.com/watch?v=aLKqIruMcrY&t=33s
        #https://www.youtube.com/watch?v=dyg6u2EyLOQ&t=39s
        #i want to simulate and track traffic behavior of tcp global synch VS wred
        #WRED+CBWFQ+LLQ+policing can all be used at the same time to form a full solution 
        frozenset({"voice"}):['one-way delay < 150ms,\njitter < 30ms,\nloss < 1%'],
        frozenset({"video"}):['one-way delay: 200-400ms,\njitter: 30-50ms,\nloss: 0.1-1%'],
        frozenset({"tail drop"}):['what is it called when packets at the back of a queue are dropped as a consequence of it being full. default congestion management behavior'],
        frozenset({"fifo"}):['by default, in what manner are messages queued & forwarded?'],
        #"wred":['above a threshold of congestion (queue fullness), randomly select packets to drop as opposed to "tail drop". different classes of packets have different probabilities of being dropped'],
        #actually not sure how wred works - do the classifications make certain packets have a higher chance of being dropped, or do they make it so only lower priority or both lower & higher packets are randomly dropped - depending on the congestion threshold reached?
        frozenset({"classification"}):['identify and categorize traffic in order to perform particular actions on it, or so it can be marked for another device to perform those actions'],
        frozenset({"marking"}):['modify headers as a result of classification, so upstream devices expend less cpu to determine QoS actions'],
        frozenset({'queuing'}):['placing received packets in a buffer before sending. the buffer follows FIFO logic by default.'],
        frozenset({'scheduling'}):['the function or algorithm that deceides from which queue to send from next'],
        frozenset({'round robin'}):['scheduling algorithm that sends from each queue at the same rate and in turns'],
        frozenset({'weighted round robin'}):['scheduling algorithm that sends from each queue at different rates, but in turns'],
        frozenset({'CBWFQ'}):['a type of weighted round robin that garuantees a minimum amount of bandwidth to each queue during congestion'],
        #CBWFQ are bad for low jitter/delay traffic. LLQs solve this problem. they can be used at the same time: 3 CBWFQ qs and 1 LLQ. 
        #during times of no congestion, CBWFQ apparently does nothing https://community.cisco.com/t5/switching/cbwfq-in-non-congestion-network/td-p/3022303
        frozenset({'LLQ'}):['a queue that is always sent from first. used for low latency traffic like voice. called "strict priority queue" '],
        #difference between queuing and scheduling?
        frozenset({'congestion'}):['when queues become full'],
        frozenset({'policing'}):['drops packets when traffic rate gets too high. can be configured to mark packets instead. prevent LLQs from starving other queues. limits customer\'s bandwidth'],
        frozenset({'shaping'}):['buffers & delays packets when the traffic rate gets too high. used by customers'],
        frozenset({'DSCP'}):['6 bit ipv4 marking, replaces IPP'],
        frozenset({'CoS'}):['3 bit marking field in the dot1q header, and is only used on trunk & voip links. AKA "PCP"'],
        frozenset({'NBAR'}):['uses deep packet inspection to classify packets based on (up to) Layer 7 information'],
        frozenset({'ToS'}):['8 bit ipv4 header that contains DSCP and ECN fields, and legacy: IPP field'],
        frozenset({'IPP'}):['3 bit legacy ipv4 marking. replaced by DSCP'],
        frozenset({'Default Forwarding'}):['DSCP value 000000, also known as "best effort traffic"'],
        frozenset({'Expedited Forwarding'}):['DSCP value 101110 or 46. low latency/loss/jitter, e.g., voice traffic'],
        frozenset({'Assured Forwarding'}):['A range of DSCP values: xxxyy0 which determine class (x) and drop presendence (y)'],
        frozenset({'Class Selector'}):['DSCP values: xxx000. enable backward compatibility with IPP'],
        frozenset({'trust boundary'}):['a place on the network that figuratively separates from which devices DSCP markings will be trusted, and which will be replaced/untrusted.']
},
    'ports':{
    frozenset({"tcp 20"}):['ftp data'],
    frozenset({"tcp 21"}):['ftp control'],
    frozenset({"tcp 22"}):['ssh'],
    frozenset({"tcp 23"}):['telnet'],
    frozenset({"tcp 25"}):['smtp'],
    frozenset({"udp tcp 53"}):['dns'],
    frozenset({"udp 67"}):['dhcp server'],
    frozenset({"udp 68"}):['dhcp client'],
    frozenset({"udp 69"}):['tftp'],
    frozenset({"tcp 110"}):['pop3'],
    frozenset({"udp 123"}):['ntp'],
    frozenset({"udp 161"}):['snmp'],
    frozenset({"udp 514"}):['syslog'],
    frozenset({'udp 49'}):['tacacs+'],
    frozenset({'udp 1812'}):['radius authentication'],
    frozenset({'udp 1813'}):['radius accounting']
},
    'routing_AD':{          
    frozenset({'Connected'}): [0],       
    frozenset({'Static'}): [1],                             
    frozenset({'eBGP'}): [20],                
    frozenset({'EIGRP'}): [90],                 
    frozenset({'OSPF'}): [110],                
    frozenset({'IS-IS'}): [115],                 
    frozenset({'RIP'}): [120],               
    frozenset({'external EIGRP'}): [170],                          
    frozenset({'iBGP'}): [200],                
    frozenset({'DHCP'}): [254],                
    frozenset({'unroutable'}): [255],                    
},
    'wan':{
        frozenset({'hub and spoke'}):['what WAN architecture has all other edge routers connect to a central router, but not each other?'],
        frozenset({'MPLS'}):['what technology is used by SPs to isolate customer traffic, and forwards/routes using labels instead of IP addresses?'],
        frozenset({'Provider Edge'}):['In MPLS, what do we call the SP\'s device that connects with the customer\'s? write the unabbreviated term'],
        frozenset({'Customer Edge'}):['In MPLS, what do we call the customer\'s device that connects with the SP\'s? write the unabbreviated term'],
        frozenset({'Provider core'}):['In MPLS, what device is denoted as \'P router\' in the SP\'s network? write the unabbreviated term'],
        #jeremy IT labs talks about l2 MPLS being a big switch, while OCG talks about metroE being a big switch
            #also calls the routing protocol peering version 'l3 mpls vpn'
        # 'L2':['which mpls vpn makes the SP\'s network seem like a big switch to the customer, putting both CEs on the same subnet?'],
        frozenset({'metro ethernet'}):['which WAN service makes the SP\'s edge seem like a big switch to the customer, putting both CEs on the same subnet?'],
        frozenset({'MPLS vpn'}):['what WAN technology leverages MP-BGP, route redistribution, VRFs and has CEs and PEs become routing protocol neighbors?'],
        #CATV, DSL
        frozenset({'DSL'}):['what service connected customers to the internet over phone lines using a modem?'],
        frozenset({'CATV'}):['what service connected customers to the internet over \'cable\' television lines using a modem?'],
        #VPNs
        frozenset({'site-to-site'}):['type of VPN that uses tunnel mode to connect two private networks over the internet as if they are virtually directly connected.'],
        frozenset({'IPsec'}):['What is the layer 3 security framework used to construct VPNs'],
        frozenset({'remote access'}):['type of VPN that uses transport mode to connect a single client over the internet to a private network'],
        frozenset({'tunnel'}):['IPsec mode that encrypts everything L3+, and adds an outside IP information'],
        frozenset({'transport'}):['IPsec mode that only encrypts everything above L3'],
        frozenset({'tls'}):['what kind of VPN is an alternative to IPsec for remote access VPNs?'],
        #these are mentioned in jeremny it labs, but not in OCG
        # 'single homed' : ['what is it called when a customer only has one connection to a service provider'], 
        # 'dual homed ' : [''], 
        # 'multi homed' : [''], 
        # 'dual multihomed' : [''], 

            #there are e-line, e-lan, e-tree, wireless WAN (4,5,6g, etc) topics in the OCG, but seems like these arent on the exam
},
    'wireless':{
    #WPA1,2,3 details, CCMP & GCMP
    frozenset({'split-mac'}):['architecture that involves multiple LAPs controlled by a WLC'],
    frozenset({'autonomous'}):['___ AP that operates in a standalone/independent manner','what kind of mode do Meraki APs typically use (surprisingly)'],
    frozenset({'cloud'}):['what type of architecture does Meraki fit into?', 'what deployment model is a centralized model, but specifically leverages cloud?'],
    frozenset({'centralized'}):['what deployment model places a wlc in a central, likely remote, location to support a large number of APs/clients?'],
    frozenset({'distributed'}):['what deployment model distributes multiple WLCs across a campus in places down stream from a central-ish location?'],
    frozenset({'embedded'}):['what deployment model has WLC software run on non-dedicated WLC hardware? e.g., wlc running on a switch'],
    frozenset({'mobility express'}):['what is cisco\'s feature that enables WLCs to be embedded on on LAPs?'],
    #modes 
    frozenset({'Local'}):['Default mode for a LAP that provides a BSS, sends client data to WLC and other info regarding rogue devices, noise/interference, stuff for WIDS'],
    frozenset({'Monitor'}):['mode where the AP only listens. captures frames to check for IDS events, detects rogue APs, something about ...  detecting stations through location based sevices ¯\\_(ツ)_/¯'],
    frozenset({'FlexConnect'}):['mode where an AP can forward traffic on its local network without CAPWAP trip while still being controlled remotely. Can act autonomously when losing connection with WLC.'],
    frozenset({'Sniffer'}):['mode where an AP captures 802.11 traffic to send to a an analyzer (e.g., wireshark)'],
        #note:jeremy'sITlab says rogue detector listen only to wired, OCG says it listens to both wired and wireless 
    frozenset({'Rogue detector'}):['mode that listens to the wired network for mac addresses. makes correlations to detect rogue APs'],
    frozenset({'Bridge'}):['mode that connects different networks wirelessly. e.g., 2 APs connect to each other.'],
    frozenset({'SE-Connect'}):['mode that listens to RF data and sends it to a spectrem analyzer'],
    #security
    frozenset({'open authentication'}):['what \'authentication\' method allows user to connect to the BSS unconditionally? used today with login portal behind it, but no encryption'],
    frozenset({'WEP'}):['what wireless encryption/authentication method is insecure/old, used a shared key, and leveraged RC4?'],
    frozenset({'EAP'}):['an authentication \'framework\' that supports multiple different authentication methods'],
    frozenset({'802.1x'}):['basically just EAP over LAN (EAPoL)'],
    frozenset({'TKIP'}):['an enhancement to WEP intended as a temporary solution until an improvement over WEP was developed/ratified.'],
    frozenset({'CCMP'}):['a wifi security protocol that uses AES counter mode & CBC-MAC'],
    frozenset({'GCMP'}):['WPA3\'s wifi security protocol that uses AES counter mode & GMAC'],
    frozenset({'PMF'}):['prevents abuse of management frames. optional in WPA2, mandatory in WPA3.'],
    frozenset({'SAE'}):['added security for PSK in WPA3. protects the 4way handshake.'],
    frozenset({'forward secrecy'}):['past messages that have been captured cannot be practically decrypted by unauthorized entity'],
    frozenset({'option 43'}):['configuration on a dhcp server that tells access points the IP of their controller'],
},
    'security':{
        #password shit, ssh, etc
        #dhcp snooping 
        frozenset({'option 82'}):['what feature interferes with dhcp when the dhcp snooping switch isn\'t also a relay agent?'],
        frozenset({'no ip dhcp snooping information option'}):['what command stops dhcp snooping from inserting relay header?'],
        frozenset({'dhcp snooping binding table'}):['what does dhcp snooping use to keep track of dhcp leases?'],
        frozenset({'trusted'}):['what kind of dhcp snooping/DAI port allows inbound DHCP server messages?'],
        frozenset({'untrusted'}):['what kind of dhcp snooping/DAI port is every port by default?'],
        frozenset({'ip dhcp snooping'}):['what command enables dhcp snooping, and needs to be entered before related configurations will work?'],
        frozenset({'ip dhcp snooping vlan 5'}):['after enabling, what command that specifies dhcp snooping should be applied to vlan 5?'],
        frozenset({'ip dhcp snooping trust'}):['what interface command makes that interface a dhcp snooping trusted port?'],
        frozenset({'show ip dhcp snooping binding'}):['what command shows dhcp lease information tracked by dhcp snooping?'],
        frozenset({'ip dhcp snooping limit rate 3'}):['what interface command rate limits dhcp messages to 3 per second?'],
        frozenset({'errdisable recovery cause dhcp-rate-limit'}):['what command configures automatic recovery from dhcp snooping rate limit violation?'],
        frozenset({'disabled'}):['is dhcp snooping rate limiting enabled or disabled by default'],
        #dai
        frozenset({'dhcp snooping'}):['what other security feature is DAI dependant on by default?'],
        frozenset({'ip arp inspection vlan 3'}):['after enabling dhcp snooping, what command enables dai on vlan 3?'],
        frozenset({'ip arp inspection trust'}):['what interface command makes a port DAI trusted?'],
        frozenset({'15'}):['what is the default DAI rate limit? (number: arps per second)'],
        frozenset({'ip arp inspection limit rate 16 burst interval 3'}):['what interface command leverages DAI\'s "burst interval" to precisely configure 16 arp messages per 3 seconds?'],
        #theres also validation options, which i cbf putting in rn. https://youtu.be/HwbTKaIvL6s?si=ziT4bT3DvQiybdW7&t=996
        #should be noted all 3 can be enabled at the same time, but only as a 1-liner as opposed to 3 commands
        #port security
        frozenset({'protect'}):['which port-security mode just discards, and does not increment the violation counter?', 'which port-security mode does not increment the violation counter?'],
        frozenset({'restrict'}):['which port-security mode just discards, and logs?'],
        frozenset({'shutdown'}):['which port-security mode just discards, logs, and shuts(errdisable)?', 'which is the default port-security violation mode'],
        frozenset({'switchport port-security'}):['what interface command enables port-security on that interface?'],
        frozenset({'switchport port-security violation restrict'}):['what interface command sets the port-security mode to restrict?'],
        frozenset({'switchport port-security mac-address aaaa.bbbb.cccc'}):['what interface command statically configures mac-address aaaa.bbbb.cccc to be allowed by port-security?'],
        frozenset({'switchport port-security mac-address sticky'}):['what interface command configures dynamic learning of mac-addresses, which never age-out? (port-security)'],
        #statically configuring a mac address will increase the total mac counter, reducing the amount of dynamically learned macs allowed
        #sticky-learned macs need a 'copy run start' to be persistant between reloads
        #apparently the sticky command will also immediately convert dynamically learned addresses to sticky ones -jeremyITlabs
        #the opposite will happen if you disable sticky learning with 'no'
        frozenset({'switchport port-security maximum 8'}):['port-security command sets the maximum number of allowed addresses to 8 on an interface?'],
        #this maximum is macs that map to that port
        frozenset({'1'}):['what is the default maximum mac addresses allowed by port security'],
        #must be statically configured access or trunk
        frozenset({'no'}):['can port security be enabled on DTP ports?'],
        frozenset({'switchport mode access'}):['what interface command should be used on an edge port so that enabling port security will work?'],
        frozenset({'show port-security interface g0/1'}):['what command shows port-security details of port g0/1'],
        frozenset({'show port security'}):['what command shows a brief format of all ports\' port-security details'],
        frozenset({'errdisable recovery cause psecure-violation'}):['what command configures automatic errdisable recovery for port security violations?'],
        frozenset({'300'}):['what is the default err-disable recovery time?'],
        frozenset({'errdisable recovery interval 100'}):['what command adjusts err-disable recovery time to 100 seconds?'],
        #can verify with 'show errdisable'
},
    'ipv6':{
    #NEED TO DO :'solicited node multicast':[''],

    #other things besides quiz to strengthen ipv6 skills:
    #hex conversion, shortening/expanding addresses, subnetting (what about it though?)
    #interface command: ipv6 enable - generates link local address on interface, but does it do anything else?
    #solicited node address generation https://youtu.be/rwkHfsWQwy8?si=vb7WdkVrUlU6ndP-&t=594

    #link-local refers to the broadcast domain, not just the single physical link 
    #address ranges
    #https://www.youtube.com/watch?v=hJ7Mc3LLWXI
    frozenset({'solicited node multicast'}):['what kind of address is used to request/discover a mac address associated with an ipv6 address?'],
    frozenset({'unique local'}):['what kind of address starts with numbers in the range of FC-FD?', 'what is the ipv6 name for private addresses?'],  
    frozenset({'FD'}):['due to some odd rules, what should the first 2 characters of ULA addresses be *in practice*'],  
    frozenset({'link local'}):['which kind of address starts with FE80?'], 
    frozenset({'multicast'}):['which kind of ipv6 address begins with FF'],
    frozenset({'loop back'}):['what kind of address is ::1'],
    #multicast ranges ?
    frozenset({'interface-local'}):['what is the scope of FF01 addresses?'],
    frozenset({'link-local'}):['what is the scope of FF02 addresses?'],
    frozenset({'ipv6 address fe80::69 link-local'}):['what command configures a specific link local address: fe80::69'],
    
    frozenset({'FF02::1:ffb4:5b6d'}):['what solicited node multicast address will be created if an interface has this address 2001:db8::a1c2:d3b4:5b6d/64'],
    frozenset({'MDN snooping'}):['what do switches need to have enabled to prevent multicast\'s from be flooded out every port?'],
    frozenset({'FF02::1:FF'}):['what part of solicited multicast addresses is the same in every one?'],
    frozenset({'ipv6 enable'}):['what command automatically generates/assigns a link local address on an interface?'],
    #FF02::1:FFxx:xxxx
    #FF02::1 is very different from FF02::1:FF 
    #!!!what is the usecase of solicited nodemulticast? apparently its for when a computer doesn't know it's default gateways mac address.
    frozenset({'FF02::1'}):['what is the \'all nodes\' ipv6 multicast address?'],
    frozenset({'FF02::2'}):['what is the \'all routers\' ipv6 multicast address?'],
    frozenset({'FF02::5'}):['what is the all OSPF routers ipv6 multicast address?'],
    frozenset({'FF02::6'}):['what is the all OSPF BRs/BDRs ipv6 multicast address?'],
    frozenset({'site-local'}):['what is the scope of FF05 addresses?'],
    frozenset({'organization-local'}):['what is the scope of FF08 addresses?'],
    frozenset({'global'}):['what is the scope of FF0E addresses?'],
    frozenset({'global unicast'}):['what kind of ipv6 address starts with 2 or 3 and is in the range of 2000::/3?', 'what is the ipv6 name for public addresses?'],
    frozenset({'anycast'}):['what kind of ipv6 address is one-to-nearest?'],
    frozenset({'::/0'}):['what ipv6 address is used in default routes in place of 0.0.0.0?'],
    #ndp
    frozenset({'ndp'}):['what is used in place of arp for IPv6?'],
    frozenset({'neighbor solicitation'}):['what is the ipv6 equivalent of an arp request? (to learn mac:ip map)'],
    frozenset({'neighbor advertisement'}):['what is the ipv6 equivalent of an arp reply? (to provide mac:ip map)'],
    frozenset({'show ipv6 neighbor'}):["what command shows ipv6 to mac mappings"],
    frozenset({'router solicitation'}):['what type of message uses FF02::2 to discover local routers?'],
    frozenset({'router advertisement'}):['what type of message uses FF02::1 by routers to inform local devices of it\'s presence?'],
    #dhcpv6,slaac,eui
        ####modified eui exercise. (generate mac -> process into interface ID -> query user on the interface ID)
        frozenset({'ipv6 address 2001:db8::/64 eui-64'}):['what interface command uses eui-64 to assign an address from the 2001:db8::/64 network?'],
        frozenset({'A3C2:D3FF:FEB4:5B6D'}):['write the EUI-64 interface ID that will be created from this mac address: A1C2.D3B4.5B6D'], #rng the mac address and ask more than once ?
        #note most of the 'global id'(network portion) of a ULA should be randomly generated, to reduce the chance of collisions when companies merge
        frozenset({'SLAAC'}):['what feature learns the network/subnet ID and prefix length from RAs and then uses EUI-64 to generate & assign a full ipv6 address?'],
        frozenset({'ipv6 address autoconfig'}):['what interface command uses SLAAC to assign an address?'],
        frozenset({'DAD'}):['upon an interface coming online or being assigned an address, what feature automatically sends an NS with that address to verify it\'s uniqueness?'],
    #subnetting - questions about /48 block assignment into /64 subnets (16 bit subnet portion)
    #global routing prefix, subnet id (aka subnet prefix), interface ID - may or maynot include these.
    frozenset({'16'}):['how many bits in each 4 digit group of an ipv6 address?'],
    frozenset({'4'}):['how many bits is a single digit in ipv6?'],
    frozenset({'ipv6 unicast-routing'}):['what command enables ipv6 routing?'],
    frozenset({'fully specified'}):['what kind of static route must be used when using link local addr as a nexthop?'],
    #commands: (e.g. show commands, & enabling ipv6 routing etc)
},
    'IPv4_multicast':{
    #224.0.0.2:HSRPv1
    frozenset({'224.0.0.10'}):['EIGRP'],
    frozenset({'224.0.0.102'}):['HSRP','GBLP'],
    frozenset({'224.0.0.18'}):['VRRP'],
    frozenset({'224.0.0.5'}):['all ospf (for sending hellos)'],
    frozenset({'224.0.0.6'}):['all ospf DR/BDR'],
    frozenset({'224.0.0.9'}):['RIP'],
},
    'fhrp':{ 
        #https://blog.boson.com/bid/106020/first-hop-redundancy-protocol-fhrp
        #not covered:
        #hold/hello timers
        #specific multicast macaddresses
        frozenset({'no'}):['do GLBP & HSRP devices pre-empt by default? (yes/no)'],
        frozenset({'gratuitous ARP'}):['upon a FHRP device taking over, how does it update switch mac tables to direct frames to the new location of the virtual mac?'],
        frozenset({'object tracking'}):['what FHRP feature tracks states of things, e.g., routing table, interface state, etc to conditionally allow another router to take over? (by lowering its priority)'],
        frozenset({'HSRP'}):[
            'which FHRP use \'active\' and \'standby\' routers?',
            'which cisco FHRP requires per-vlan/subnet configuration to load balance?',
            'which FHRP protocol uses this mac address? 0000.0C07.AC...'
        ],
        frozenset({'VRRP'}):[
            'which FHRP use \'master\' and \'backup\' routers?',
            'which FHRP is an open standard that is very similar to HSRP?',
            'which FHRP preempts by default?',
            'which FHRP protocol uses this mac address? 0000.5e00.01...'
        ],
        frozenset({'GLBP'}):[
            'which FHRP can load balance within a single subnet?',
            'which FHRP use \'AVG\' and \'AVF\' routers?',
            'which FHRP protocol uses this mac address? 0007.b400...'
        ],
        frozenset({'AVG'}):['What GLBP role leverages ARP to direct hosts to different AVFs?'],#i think in a round-robin fashion by defualt.
        frozenset({'AVF'}):['What GLBP role sends traffic, while also being a backup to the other role?']
},

    'nat':{
    frozenset({'inside local'}):['in NAT terms, what kind of address is a host\'s private IP?'],
    frozenset({'inside global'}):['in NAT terms, what kind of address sits on the outside of a private network and represents the host(s) from the inside?'],
    frozenset({'outside global'}):['in NAT terms, what kind of address sits on the outside of a remote private network network?'],
    frozenset({'outside local'}):['in NAT terms, what kind of address sits on the inside of a remote private network??'],
    frozenset({'ip nat outside'}):['what interface command sets that interface as part of the outside network?'],
    frozenset({'ip nat inside source static 192.168.0.167 100.0.0.1'}):['what command configures a static (one to one) inside translation between 192.168.0.167 to 100.0.0.1 ?'],
    frozenset({'show ip nat translations'}):['what command shows active NAT translations with a table?'],
    frozenset({'show ip nat statistics'}):['what command shows NAT statistics?'],
    #note some devices accept 'prefix-length 24' instead of 'netmask'
    frozenset({'ip nat pool poolname 100.1.1.0 100.1.1.255 netmask 255.255.255.0'}):['what command creates a pool \'poolname\' that includes all of 100.1.1.0/24 '],
    frozenset({'ip nat inside source list 1 pool poolname'}):['what command implements dynamic NAT using pool \'poolname\' and access-list 1?'],
    frozenset({'ip nat inside source list 1 pool poolname overload'}):['what command implements dynamic PAT using pool \'poolname\' and access-list 1?'],
    frozenset({'ip nat inside source list 1 interface g0/0 overload'}):['what command implements interface PAT using g0/0 and access-list 1?'],
    #command like this doesn't work: ip nat inside source static 192.168.0.168 100.0.0.1 overload
},
    'ntp':{
    frozenset({'ntp master 8'}):['what command sets the device as an NTP server, with the stratum level 8'],
    frozenset({'ntp server 1.2.3.4'}):['what command sets the device as an NTP client of the ip 1.2.3.4'],
    frozenset({'show clock'}):['what command shows the current time?'],
    frozenset({'show ntp status'}):['what command shows whether the clock is syncronized, device\'s stratum, and ip of the ntp device being referenced?'],
    frozenset({'show ntp associations'}):['what command shows the information of the ntp servers being referenced?'],
    frozenset({'*'}):['in output from \'show ntp associations\', what symbol is used to show which IP the device is synced with?'],
    frozenset({'address'}):['what column of \'show ntp associations\' shows the ip address of the ntp server?'],
    frozenset({'ref clock'}):['what column of \'show ntp associations\' shows the ip address that the ntp server is a client of? (the server to the server.)'],
    frozenset({'.locl.'}):['if a device is master and \'show ntp associations\' has been entered, what is seen in the ref column?'],
    frozenset({'127'}):['what is the first octet of the address that shows up in the ref clock column when \'show ntp associations\' is entered on a client device of an NTP master?'],
    frozenset({'ntp source lo0'}):['what command sets loopback lo0\'s address as the ntp server address?'],
    #apparently theres an alternative 'calendar set' command that sets the 'hardware clock' as opposed to the 'software clock' ??? no idea what this means as OCG didnt mention it
    #also 'clock update-calendar' syncs the calendar to the clock time. 'clock read calendar' syncs the clock to the calendar time.
    frozenset({'clock set 12:32:00 19 January 2023'}):['what command sets the device\'s utc-0 time to 12:32:00 19 january 2023?'],
    frozenset({'clock timezone EST -5'}):['what command offsets the learned or set utc-0 time by -5 and gives a human readable timezone note \'EST\'?'],
    frozenset({'clock summer-time EST recurring'}):['what command configures the start and end of daylight saving time. use EST as the human readable timezone.'], 
    #note ^the answer here is the command the ocg gave and didnt explain anything about its default behavior, so its not clear what this command does when not specifying the start/end of daylight saving, which can be specified as args.
    #e.g. 'clock summer-time EDT recurring 2 sunday march 02:00 1 sunday november 02:00'
    frozenset({'15'}):['what is the maximum stratum?'],
    frozenset({'symmetric active mode'}):['what ntp mode peers with devices on the same stratum for better accuracy?'],
    frozenset({'ntp peer 1.2.3.4'}):['what command leverages symmetric active mode by peering with a device (IP: 1.2.3.4) of the same stratum?'],
    frozenset({'primary server'}):['what is the name of stratum 1 devices that get their time from reference clocks (stratum 0 devices)?']
    #NTP authentication: i'm guessing this isnt on the exam.
},
    'cdp_lldp':{
    frozenset({'60'}):['by default how often are cdp messages sent? (seconds) - the \'timer\' value'],
    frozenset({'180'}):['by default how long does cdp wait before removing a neighbor from the cdp table? (seconds) - the \'holdtime\' value'],
    frozenset({'show cdp'}):['what command shows the cdp \'global\' timer and holdtime?'],
    frozenset({'show cdp interface'}):['what command shows the cdp timer & holdtime for each interface?'],
    frozenset({'show cdp traffic'}):['what command shows cdp stats'],
    frozenset({'show cdp neighbor detail'}):['what cdp command shows extra detail about neighbors'],
    frozenset({'no cdp run'}):['what command disables cdp globally?'],
    frozenset({'cdp enable'}):['what command enables CDP on a specific interface?'],
    frozenset({'cdp timer 59'}):['what command sets cdp timer to 59 seconds?'],
    frozenset({'cdp holdtime 179'}):['what command sets cdp holdtime to 179 seconds?'],
    frozenset({'30'}):['by default how often are LLDP messages sent? (seconds) - the \'timer\' value'],
    frozenset({'120'}):['by default how long does LLDP wait before removing a neighbor from the LLDP table? (seconds) - the \'holdtime\' value'],
    frozenset({'lldp run'}):['what command enables lldp globally?'],
    frozenset({'show lldp interface'}):['what command shows tx/rx configuration of each interface?'],
    #this enables transmission/reception on all interfaces according to PT behavior, which is contrary to jeremyITlab statements
    frozenset({'no lldp transmit'}):['what command disables sending lldp on a specific interface?'],
    #lldp, timer, holdtime, & show commands are the same
    #R,S are used for router and switch for CDP. LLDP uses R,B(ridge)
},
    'dhcp':{
        #show lease, show binding table
        frozenset({'ip dhcp pool poolname'}):['what command enters dhcp config mode for a pool named \'poolname\'?'],
        frozenset({'default-router 192.168.0.1'}):['once in dhcp config mode for a pool, what command configures the default router address 192.168.0.1 for that pool?'],
        frozenset({'dns-server 1.1.1.1'}):['once in dhcp config mode for a pool, what command configures the dns address 1.1.1.1 for that pool?'],
        frozenset({'network 192.168.1.0 255.255.255.0'}):['once in dhcp config mode for a pool, what command configures 192.168.1.0/24 to be the subnet to lease from?'], 
        frozenset({'ip dhcp excluded-address 192.168.1.1 192.168.1.10'}):['what command excludes addresses 192.168.1.1 to .10 from being leased by dhcp?'],
        frozenset({'ip helper-address 69.69.69.69'}):['what command configures an interface to relay dhcp messages to a dhcp server:69.69.69.69'],
        frozenset({'domain-name example.com'}):['what pool command tells clients the domain they\'re apart of is example.com?'], 
        # need to find out what 'domain-name [name]' actually does in ip pool config mode
        # tells the client the domain name it is apart of e.g., example.com 
        # https://youtu.be/hzkleGAC2_Y?si=r3lK_KMUX2uPfs7l&t=1428 #https://info.support.huawei.com/hedex/api/pages/EDOC1100334321/AEM1020X/05/resources/dc/dhcp_server_domain-name.html
        # honestly no idea wtf this means 
        # apparently the field is called dhcp option 15
},

#doubt the cable stuff matters.
#took some screenshots of their code names etc. can be found in downloads folder
# 'cables':{
#         frozenset({''}):[''],
#     }
}#



# snmp = {#

# }
# wlc_interfaces = {}