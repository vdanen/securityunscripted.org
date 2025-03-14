Title: E06: Best practices for containers
Author: Security Unscripted
Date: 2025-03-14 09:00
Category: Podcast
Tags: container, virtual machine, vulnerability
Slug: e06-best-practices-for-containers
Status: published


When is a best practice not a best practice?  Sadly, often when we talk about containers.  Containers had a very simple promise: better security through discrete process isolation.  One process or application per container.  What have we done?  Crammed as many things into a container to run together so we've basically turned containers into lightweight virtual machines.  When did this happen?  Why?  And how can we realize the promise of better security using containers the way they were designed to be used?  It starts by understanding what they are, and why a vulnerability in a properly-designed container is so fundamentally different from the same vulnerability on bare metal or in a virtual machine.  Vincent Danen and Subhro Kar sit down to discuss this disturbing trend of using containers in a way they were not designed to be used, and how we actually make security worse.

{% youtube fPxYUTD717Q %}

References:

* [5 more reasons to run Kubernetes in your Linux homelab](https://opensource.com/article/21/6/kubernetes-linux-homelab)
* [Containers are not VMs](https://www.docker.com/blog/containers-are-not-vms/)
* [An introduction to FreeBSD Jails](https://freebsdfoundation.org/freebsd-project/resources/introduction-to-freebsd-jails/)
* [The IPC namespace on the host should remain isolated from containers](https://docs.datadoghq.com/security/default_rules/cis-docker-1.2.0-5.16/)
* [Red Hat’s Chris Jenkins on Upping Security with Containers](https://cybermagazine.com/articles/red-hats-chris-jenkins-on-upping-security-with-containers)
* [What Do the Worst Breaches in History All Have in Common?](https://blog.ariacybersecurity.com/blog/what-do-the-worst-breaches-in-history-all-have-in-common)
* [LXC container security](https://linuxcontainers.org/lxc/security/)
* [Is Having Ssh into a Docker container a Good Idea ?](https://www.reddit.com/r/docker/comments/15impwm/is_having_ssh_into_a_docker_container_a_good_idea/?rdt=38547)
* [Container Security: 7 Key Components and 8 Critical Best Practices](https://www.tigera.io/learn/guides/container-security-best-practices/#Container_Security_Best_Practices)

