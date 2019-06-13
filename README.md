# Module-2
Lab's instructions
For dns spoofing there some prerequirements:
  1. apt-get install build-essential python-dev libnetfilter-queue-dev
  2. pip install NetfilterQueue

# For Spoof Reproducing:
1. run arp_spoof
2. Run on attacker:
  a. echo 1 > /proc/sys/net/ipv4/ip_forward
  b. iptables -I FORWARD -j NFQUEUE --queue-num 0
3. run dns_spoof
4. Configure apache2 server: systemctl start apache2
5. Open URL in browser
