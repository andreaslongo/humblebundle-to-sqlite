from typing import Any

import pytest


@pytest.fixture
def expected_bundles() -> list[dict[str, Any]]:
    return [
        {
            "id": "1e9c1a9a064e4f2b10e9b434fe2ea6bbd7faabf0",
            "url": "/books/witchcraft-magick-and-spirituality-books",
            "category": "books",
            "name": "Witchcraft, Magick, and Spirituality",
            "start_date": "2021-09-30T18:00:00",
            "end_date": "2021-10-21T18:00:00",
            "description": (
                "There’s more to life than meets the eye... - Life isn’t the"
                " straightforward journey we all believe it to be. There is so much"
                " about our world, our solar system, and our universe we don’t"
                " understand. There are mysteries and magic in every corner of our"
                " world, and we’ve collected some of that mystical knowledge up for you"
                " to get your hands on, no travel required! Thanks to our partners at"
                " Hay House, Weiser Books, and HarperCollins, it's easier than ever to"
                " explore spirituality, magick, and elements of witchcraft with ebooks"
                " like <em>Wicca Made Easy</em>, <em>Wishcraft</em>, <em>Witchery</em>,"
                " and <em>Year Of The Witch</em>. Plus, your purchase helps support a"
                " charity of your choice!"
            ),
        },
        {
            "id": "8150dafead282874b62538b3f5394f792c79dbb4",
            "url": "/books/james-bond-and-beyond-dynamite-books",
            "category": "comics",
            "name": "James Bond and Beyond by Dynamite",
            "start_date": "2021-09-27T18:00:00",
            "end_date": "2021-10-18T18:00:00",
            "description": (
                "The name’s Bond... - Suave, sophisticated, and downright scary to his"
                " enemies, James Bond is 007 and one of Her Majesty’s most effective"
                " agents. With No Time To Die hitting theatres, we thought there was no"
                " better time to deliver a Dynamite Comics bundle, packed with comics"
                " like <em>James Bond 007 Vol. 2</em>, <em>James Bond Vol. 1:"
                " Vargr</em>, <em>James Bond: Casino Royale</em>, and <em>James Bond:"
                " Reflections of Death</em>.   And while Bond is saving the world once"
                " again, you’ll be helping to save lives, as your purchase supports"
                " Doctors Without Borders and a charity of your choice!"
            ),
        },
        {
            "id": "c80bc455fed1f6da530a50bb527ea49c790c3bc8",
            "url": "/books/infrastructure-and-ops-oreilly-books",
            "category": "books",
            "name": "Infrastructure and Ops by O'Reilly",
            "start_date": "2021-10-04T18:00:00",
            "end_date": "2021-10-25T18:00:00",
            "description": (
                "Master the modern IT environment - Modern technology has changed the"
                " way we live and work. Developing systems, applications, and more is"
                " complex, but O'Reilly are showing us how to get stuff done in our"
                " newest bundle, Infrastructure and Ops by O'Reilly!   Dive into ebooks"
                " like <em>Kubernetes Operators</em>, <em>Learning Helm</em>,"
                " <em>Kubernetes Best Practices</em>, and <em>Distributed Systems with"
                " Node.js</em>, and learn how to shape our digital world to suit you,"
                " both in and out of work! Plus, your purchase helps support Code for"
                " America!"
            ),
        },
        {
            "id": "ecd2302ba58b0de910896d939be8b1800bf95368",
            "url": "/books/frog-god-5e-physical-books",
            "category": "books",
            "name": "Tomes of Lost Magic for 5th Edition by Frog God Games",
            "start_date": "2021-09-23T18:00:00",
            "end_date": "2021-10-14T18:00:00",
            "description": (
                "Expand your tabletop world, with Frog God Games! - Sure, you might"
                " have the original sourcebooks. And sure, you might not have finished"
                " that one-shot that was only meant to last a session or two (we’ve all"
                " been there). You might even be between campaigns and looking for"
                " something new. Wherever you find yourself in your 5th Edition"
                " sessions, you’ve barely scratched the surface of what you can explore"
                " or imagine! Frog God Games have joined forces with Humble to deliver"
                " a bundle of spectacular value, all with the aim of expanding your 5e"
                " universe. Within the bundle, you’ll discover ebooks like <em>Book of"
                " Lost Spells (2nd Printing)</em>, <em>Tome of Alchemy</em>, <em>The"
                " Red Opera</em>, and <em>Tokens of Horror 2020</em> that add anything"
                " from new towns and places to explore to entirely new spells and"
                " monsters to face off against!  Your purchase will also help support"
                " Hospice of the Northwest and a charity of your choice!"
            ),
        },
        {
            "id": "3f61460f1f7840fc5ad532f19128b82348b3e97e",
            "url": "/books/devops-packt-books",
            "category": "books",
            "name": "The Ultimate DevOps Bundle by Packt",
            "start_date": "2021-10-11T18:00:00",
            "end_date": "2021-11-01T18:00:00",
            "description": (
                "Upgrade your DevOps toolkit! - Expand your DevOps knowledge thanks to"
                " Packt ebooks including <em>Learn Kubernetes Security</em>, <em>Azure"
                " DevOps Explained</em>, <em>Kubernetes and Docker - An Enterprise"
                " Guide</em>, and <em>Mastering Kubernetes</em>. Plus, your purchase"
                " helps support Save The Children!"
            ),
        },
        {
            "id": "eb771af650084c1fecb7e5e71423bc7b39e218e5",
            "url": "/books/ai-machine-learning-toolkit-books",
            "category": "books",
            "name": "AI & Machine Learning Toolkit",
            "start_date": "2021-10-07T18:00:00",
            "end_date": "2021-10-28T18:00:00",
            "description": (
                "AI is everywhere! - Morgan & Claypool believe that Artificial"
                " Intelligence is being integrated and discussed in areas as diverse as"
                " politics and healthcare. At the same time, enrollment in computer"
                " science has never been higher and students are flocking to AI"
                " courses. To help start your journey in this field, we’ve teamed up to"
                " provide you with books like <em>Introduction to Graph Neural"
                " Networks</em>, <em>Introduction to Semi-Supervised Learning</em>, and"
                " <em>Adversarial Machine Learning</em>. Plus, your purchase helps"
                " support Save The Children!"
            ),
        },
        {
            "id": "587cef4f562b6cda8370029331e2e387c5107e46",
            "url": "/games/play-pink-best-asmodee-digital",
            "category": "games",
            "name": "Play Pink, The Best of Asmodee Digital",
            "start_date": "2021-10-08T18:00:00",
            "end_date": "2021-10-29T18:00:00",
            "description": (
                "Play Pink, Save Lives, Enjoy Asmodee Games! - Asmodee Digital is"
                " joining us to help support the ongoing efforts to overcome breast"
                " cancer, and we’re doing the thing we do best - bundling up great"
                " games! Together, we’ve made an incredible collection including the"
                " digital editions <em>A Game of Thrones: The Board Game</em>,"
                " <em>Scythe</em>, and <em>Terraforming Mars</em>. Now’s the perfect"
                " time to grab some friends, hop online, and enjoy the best digital"
                " board games around, while you help support the Breast Cancer Research"
                " Foundation!"
            ),
        },
        {
            "id": "1e9656d7ec3bf740c7ea8bac68d880a98d66e17a",
            "url": "/software/unity-fps-games-and-game-dev-assets-software",
            "category": "software",
            "name": "UNITY FPS Games and Game Dev Assets",
            "start_date": "2021-09-16T18:00:00",
            "end_date": "2021-10-14T18:00:00",
            "description": (
                "Call the shots. - Humble Bundle and Unity have joined forces to bring"
                " you top-notch tools and art packs for your next FPS project. Take"
                " advantage of massive savings on great assets, all while contributing"
                " to sustainable initiatives worldwide. Then, enter the<span"
                ' style="color: #169fe3;">&nbsp;<a style="color: #169fe3;"'
                ' href="https://play.unity.com/discover/showcases/2021-unity-x-humble-bundle-showcase"'  # noqa: B950
                ' target="_blank">Unity x Humble Bundle Showcase</a></span> for a'
                ' chance to share your creation on <a style="color:'
                ' #169fe3;"href="http://play.unity.com/"'
                ' target="_blank">play.unity.com</a> and have it livestreamed on'
                " Twitch!"
            ),
        },
        {
            "id": "9f2748a339fc674d36be2e76b8ea0293275b7848",
            "url": "/software/javascript-software",
            "category": "software",
            "name": "Javascript",
            "start_date": "2021-10-07T18:00:00",
            "end_date": "2021-10-28T18:00:00",
            "description": (
                "$650 of JavaScript courses at your fingertips. - Learn JavaScript -"
                " the world’s most popular programming language! With this"
                " beginner-friendly bundle, you’ll learn to create your own responsive"
                " websites and modern user interfaces with CSS frameworks. You’ll build"
                " real projects, including a shopping cart app with React and a quiz"
                " game with Angular, and discover how to add 3D and AR to your web"
                " apps. You’ll even learn how to deploy your projects to the cloud -"
                " all while supporting some amazing charities. Get started now and see"
                " where web development can take you. Plus, your purchase will support"
                " Code.org and Khan Academy!"
            ),
        },
        {
            "id": "6b529d8e4e6f40b0ad312d092d1230471d71ac81",
            "url": "/software/convert-edit-record-photos-videos-gameplay-software",
            "category": "software",
            "name": "Convert, Edit, Record your Photos, Videos and Gameplay",
            "start_date": "2021-09-23T18:00:00",
            "end_date": "2021-10-14T18:00:00",
            "description": (
                "Capture, create, and convert! - Save the moments that matter to you."
                " Record them, edit them, and then convert them! In our new bundle,"
                " you’ll find everything you need to make memories, with software like"
                " Movavi Video Converter Premium 2021, Movavi Video Editor Plus 2021,"
                " and Movavi Screen Recorder 21. Plus, your purchase will support"
                " Make-A-Wish, JDRF Diabetes Foundation, and even Choose Your Own"
                " Charity!"
            ),
        },
    ]


@pytest.fixture
def expected_items() -> list[dict[str, Any]]:
    return [
        {
            "id": "70633b34aa14d37136a37758df2af193abbb96a9",
            "type": "ebook",
            "name": "Terraform: Up & Running, 2nd Edition",
            "edition": "2nd Edition",
            "author": "Yevgeniy Brikman",
            "publisher": "O'Reilly",
            "description": (
                "<p>Terraform has become a key player in the DevOps world for defining,"
                " launching, and managing infrastructure as code (IaC) across a variety"
                " of cloud and virtualization platforms, including AWS, Google Cloud,"
                " Azure, and more. This hands-on second edition, expanded and"
                " thoroughly updated for Terraform version 0.12 and beyond, shows you"
                " the fastest way to get up and running.</p><p>Gruntwork cofounder"
                " Yevgeniy (Jim) Brikman walks you through code examples that"
                " demonstrate Terraform's simple, declarative programming language for"
                " deploying and managing infrastructure with a few commands. Veteran"
                " sysadmins, DevOps engineers, and novice developers will quickly go"
                " from Terraform basics to running a full stack that can support a"
                " massive amount of traffic and a large team of"
                " developers.</p><ul><li>Explore changes from Terraform 0.9 through"
                " 0.12, including backends, workspaces, and first-class"
                " expressions</li><li>Learn how to write production-grade Terraform"
                " modules</li><li>Dive into manual and automated testing for Terraform"
                " code</li><li>Compare Terraform to Chef, Puppet, Ansible,"
                " CloudFormation, and Salt Stack</li><li>Deploy server clusters, load"
                " balancers, and databases</li><li>Use Terraform to manage the state of"
                " your infrastructure</li><li>Create reusable infrastructure with"
                " Terraform modules</li><li>Use advanced Terraform syntax to achieve"
                " zero-downtime deployment</li></ul>"
            ),
        },
        {
            "id": "0b72ce6e45c73f9a2233520decd0a3a9d817d2f3",
            "type": "ebook",
            "name": "Prometheus: Up & Running",
            "edition": None,
            "author": "Brian Brazil",
            "publisher": "O'Reilly",
            "description": (
                "<p>Get up to speed with Prometheus, the metrics-based monitoring"
                " system used by tens of thousands of organizations in production. This"
                " practical guide provides application developers, sysadmins, and"
                " DevOps practitioners with a hands-on introduction to the most"
                " important aspects of Prometheus, including dashboarding and alerting,"
                " direct code instrumentation, and metric collection from third-party"
                " systems with exporters.</p><p>This open source system has gained"
                " popularity over the past few years for good reason. With its simple"
                " yet powerful data model and query language, Prometheus does one"
                " thing, and it does it well. Author and Prometheus developer Brian"
                " Brazil guides you through Prometheus setup, the Node exporter, and"
                " the Alertmanager, then demonstrates how to use them for application"
                " and infrastructure monitoring. </p><ul><li>Know where and how much to"
                " apply instrumentation to your application code</li><li>Identify"
                " metrics with labels using unique key-value pairs </li><li>Get an"
                " introduction to Grafana, a popular tool for building"
                " dashboards</li><li>Learn how to use the Node Exporter to monitor your"
                " infrastructure </li><li>Use service discovery to provide different"
                " views of your machines and services</li><li>Use Prometheus with"
                " Kubernetes and examine exporters you can use with"
                " containers</li><li>Convert data from other monitoring systems into"
                " the Prometheus format</li></ul>"
            ),
        },
        {
            "id": "2030c64fdaa6cf6cbadd043837deaa460f9e068b",
            "type": "ebook",
            "name": "Database Reliability Engineering",
            "edition": None,
            "author": "Charity Majors, Laine Campbell",
            "publisher": "O'Reilly",
            "description": (
                "<p>The infrastructure-as-code revolution in IT is also affecting"
                " database administration. With this practical book, developers, system"
                " administrators, and junior to mid-level DBAs will learn how the"
                " modern practice of site reliability engineering applies to the craft"
                " of database architecture and operations. Authors Laine Campbell and"
                " Charity Majors provide a framework for professionals looking to join"
                " the ranks of today's database reliability engineers"
                " (DBRE).</p><p>You'll begin by exploring core operational concepts"
                " that DBREs need to master. Then you'll examine a wide range of"
                " database persistence options, including how to implement key"
                " technologies to provide resilient, scalable, and performant data"
                " storage and retrieval. With a firm foundation in database reliability"
                " engineering, you'll be ready to dive into the architecture and"
                " operations of any modern database.</p><p>This book"
                " covers:</p><ul><li>Service-level requirements and risk"
                " management</li><li>Building and evolving an architecture for"
                " operational visibility</li><li>Infrastructure engineering and"
                " infrastructure management</li><li>How to facilitate the release"
                " management process</li><li>Data storage, indexing, and"
                " replication</li><li>Identifying datastore characteristics and best"
                " use cases</li><li>Datastore architectural components and data-driven"
                " architectures</li></ul>"
            ),
        },
        {
            "id": "e8e50befcf9b795b171e7b11ef7e79f3ac3c8851",
            "type": "ebook",
            "name": "Cybersecurity Ops with Bash",
            "edition": None,
            "author": "Paul Troncone, Carl Albing",
            "publisher": "O'Reilly",
            "description": (
                "<p>If you hope to outmaneuver threat actors, speed and efficiency need"
                " to be key components of your cybersecurity operations. Mastery of the"
                " standard command-line interface (CLI) is an invaluable skill in times"
                " of crisis because no other software application can match the CLI's"
                " availability, flexibility, and agility. This practical guide shows"
                " you how to use the CLI with the bash shell to perform tasks such as"
                " data collection and analysis, intrusion detection, reverse"
                " engineering, and administration.</p><p>Authors Paul Troncone, founder"
                " of Digadel Corporation, and Carl Albing, coauthor of bash Cookbook"
                " (O'Reilly), provide insight into command-line tools and techniques to"
                " help defensive operators collect data, analyze logs, and monitor"
                " networks. Penetration testers will learn how to leverage the enormous"
                " amount of functionality built into nearly every version of Linux to"
                " enable offensive operations.</p><p>In four parts, security"
                " practitioners, administrators, and students will"
                " examine:</p><ul><li><strong>Foundations:</strong> Principles of"
                " defense and offense, command-line and bash basics, and regular"
                " expressions</li><li><strong>Defensive security operations:</strong>"
                " Data collection and analysis, real-time log monitoring, and malware"
                " analysis</li><li><strong>Penetration testing:</strong> Script"
                " obfuscation and tools for command-line fuzzing and remote"
                " access</li><li><strong>Security administration:</strong> Users,"
                " groups, and permissions; device and software inventory</li></ul>"
            ),
        },
        {
            "id": "3297498ce218b8672e0453a2b379037f6ffc6ab3",
            "type": "ebook",
            "name": "Distributed Tracing in Practice",
            "edition": None,
            "author": (
                "Austin Parker, Daniel Spoonhower, Jonathan Mace, Ben Sigelman, Rebecca"
                " Isaacs"
            ),
            "publisher": "O'Reilly",
            "description": (
                "<p>Since most applications today are distributed in some fashion,"
                " monitoring their health and performance requires a new approach."
                " Enter distributed tracing, a method of profiling and monitoring"
                " distributed applications -- particularly those that use microservice"
                " architectures. There's just one problem: distributed tracing can be"
                " hard. But it doesn't have to be.\n\nWith this guide, you'll learn"
                " what distributed tracing is and how to use it to understand the"
                " performance and operation of your software. Key players at LightStep"
                " and other organizations walk you through instrumenting your code for"
                " tracing, collecting the data that your instrumentation produces, and"
                " turning it into useful operational insights. If you want to implement"
                " distributed tracing, this book tells you what you need to"
                " know.</p><p>You'll learn:</p><ul><li>The pieces of a distributed"
                " tracing deployment: instrumentation, data collection, and"
                " analysis</li><li>Best practices for instrumentation: methods for"
                " generating trace data from your services</li><li>How to deal with (or"
                " avoid) overhead using sampling and other techniques</li><li>How to"
                " use distributed tracing to improve baseline performance and to"
                " mitigate regressions quickly</li><li>Where distributed tracing is"
                " headed in the future</li></ul>"
            ),
        },
        {
            "id": "13a1f7c85ac3552d650ffdf0976494df0e3bd5db",
            "type": "ebook",
            "name": "Kubernetes Best Practices",
            "edition": None,
            "author": "Brendan Burns, Eddie Villalba, Dave Strebel, Lachlan Evenson",
            "publisher": "O'Reilly",
            "description": (
                "<p>In this practical guide, four Kubernetes professionals with deep"
                " experience in distributed systems, enterprise application"
                " development, and open source will guide you through the process of"
                " building applications with this container orchestration system. Based"
                " on the experiences of companies that are running Kubernetes in"
                " production successfully, many of the methods are also backed by"
                " concrete code examples.</p><p>This book is ideal for those already"
                " familiar with basic Kubernetes concepts who want to learn common best"
                " practices. You'll learn exactly what you need to know to build your"
                " best app with Kubernetes the first time.</p><ul><li>Set up and"
                " develop applications in Kubernetes</li><li>Learn patterns for"
                " monitoring, securing your systems, and managing upgrades, rollouts,"
                " and rollbacks</li><li>Understand Kubernetes networking policies and"
                " where service mesh fits in</li><li>Integrate services and legacy"
                " applications and develop higher-level platforms on top of"
                " Kubernetes</li><li>Run machine learning workloads in"
                " Kubernetes</li></ul>"
            ),
        },
        {
            "id": "1938b2f660c19ffd7582ed30754c3332fb34d41a",
            "type": "ebook",
            "name": "Learning Kali Linux",
            "edition": None,
            "author": "Ric Messier",
            "publisher": "O'Reilly",
            "description": (
                "<p>With more than 600 security tools in its arsenal, the Kali Linux"
                " distribution can be overwhelming. Experienced and aspiring security"
                " professionals alike may find it challenging to select the most"
                " appropriate tool for conducting a given test. This practical book"
                " covers Kali's expansive security capabilities and helps you identify"
                " the tools you need to conduct a wide range of security tests and"
                " penetration tests. You'll also explore the vulnerabilities that make"
                " those tests necessary.</p><p>Author Ric Messier takes you through the"
                " foundations of Kali Linux and explains methods for conducting tests"
                " on networks, web applications, wireless security, password"
                " vulnerability, and more. You'll discover different techniques for"
                " extending Kali tools and creating your own toolset.</p><ul><li>Learn"
                " tools for stress testing network stacks and"
                " applications</li><li>Perform network reconnaissance to determine"
                " what's available to attackers</li><li>Execute penetration tests using"
                " automated exploit tools such as Metasploit</li><li>Use cracking tools"
                " to see if passwords meet complexity requirements</li><li>Test"
                " wireless capabilities by injecting frames and cracking"
                " passwords</li><li>Assess web application vulnerabilities with"
                " automated or proxy-based tools</li><li>Create advanced attack"
                " techniques by extending Kali tools or developing your own</li><li>Use"
                " Kali Linux to generate reports once testing is complete</li></ul>"
            ),
        },
        {
            "id": "5821694b48d0dd87ae835f7b9abdcae22e4772d7",
            "type": "ebook",
            "name": "Seeking SRE",
            "edition": None,
            "author": "David N. Blank-Edelman",
            "publisher": "O'Reilly",
            "description": (
                "<p>Organizations big and small have started to realize just how"
                " crucial system and application reliability is to their business."
                " They've also learned just how difficult it is to maintain that"
                " reliability while iterating at the speed demanded by the marketplace."
                " Site Reliability Engineering (SRE) is a proven approach to this"
                " challenge.</p><p>SRE is a large and rich topic to discuss. Google led"
                " the way with <em>Site Reliability Engineering</em>, the wildly"
                " successful O'Reilly book that described Google's creation of the"
                " discipline and the implementation that's allowed them to operate at a"
                " planetary scale. Inspired by that earlier work, this book explores a"
                " very different part of the SRE space. The more than two dozen"
                " chapters in <em>Seeking SRE</em> bring you into some of the important"
                " conversations going on in the SRE world right now.</p><p>Listen as"
                " engineers and other leaders in the field"
                " discuss:</p><ul><li>Different ways of implementing SRE and SRE"
                " principles in a wide variety of settings</li><li>How SRE relates to"
                " other approaches such as DevOps</li><li>Specialties on the cutting"
                " edge that will soon be commonplace in SRE</li><li>Best practices and"
                " technologies that make practicing SRE easier</li><li>The important"
                " but rarely explored human side of SRE</li></ul><p>David N."
                " Blank-Edelman is the book's curator and editor.</p>"
            ),
        },
        {
            "id": "a0dcbb226a390669457b679ea46568a642bfb25e",
            "type": "ebook",
            "name": "Migrating to AWS: A Manager's Guide, 1st Edition",
            "edition": "1st Edition",
            "author": "Jeff Armstrong",
            "publisher": "O'Reilly",
            "description": (
                "<p>Bring agility, cost savings, and a competitive edge to your"
                " business by migrating your IT infrastructure to AWS. With this"
                " practical book, executive and senior leadership and engineering and"
                " IT managers will examine the advantages, disadvantages, and common"
                " pitfalls when moving your company's operations to the"
                " cloud.</p><p>Author Jeff Armstrong brings years of practical hands-on"
                " experience helping dozens of enterprises make this corporate change."
                " You'll explore real-world examples from many organizations that have"
                " made -- or attempted to make -- this wide-ranging transition. Once"
                " you read this guide, you'll be better prepared to evaluate your"
                " migration objectively before, during, and after the process in order"
                " to ensure success.</p><ul><li>Learn the benefits and drawbacks of"
                " migrating to AWS, including the risks to your business and"
                " technology</li><li>Begin the process by discovering the applications"
                " and servers in your environment</li><li>Examine the value of AWS"
                " migration when building your business case</li><li>Address your"
                " operational readiness before you migrate</li><li>Define your AWS"
                " account structure and cloud governance controls</li><li>Create your"
                " migration plan in waves of servers and applications</li><li>Refactor"
                " applications that will benefit from using more cloud native"
                " resources</li></ul>"
            ),
        },
        {
            "id": "b4d461aaefbfab51e94722b6e2dfbb9eb8199135",
            "type": "ebook",
            "name": "Kubernetes Operators",
            "edition": None,
            "author": "Jason Dobies, Joshua Wood",
            "publisher": "O'Reilly",
            "description": (
                "<p>Operators are a way of packaging, deploying, and managing"
                " Kubernetes applications. A Kubernetes application doesn't just run on"
                " Kubernetes; it's composed and managed in Kubernetes terms. Operators"
                " add application-specific operational knowledge to a Kubernetes"
                " cluster, making it easier to automate complex, stateful applications"
                " and to augment the platform. Operators can coordinate application"
                " upgrades seamlessly, react to failures automatically, and streamline"
                " repetitive maintenance like backups.</p><p>Think of Operators as site"
                " reliability engineers in software. They work by extending the"
                " Kubernetes control plane and API, helping systems integrators,"
                " cluster administrators, and application developers reliably deploy"
                " and manage key services and components. Using real-world examples,"
                " authors Jason Dobies and Joshua Wood demonstrate how to use Operators"
                " today and how to create Operators for your applications with the"
                " Operator Framework and SDK.</p><ul><li>Learn how to establish a"
                " Kubernetes cluster and deploy an Operator</li><li>Examine a range of"
                " Operators from usage to implementation</li><li>Explore the three"
                " pillars of the Operator Framework: the Operator SDK, the Operator"
                " Lifecycle Manager, and Operator Metering</li><li>Build Operators from"
                " the ground up using the Operator SDK</li><li>Build, package, and run"
                " an Operator in development, testing, and production"
                " phases</li><li>Learn how to distribute your Operator for installation"
                " on Kubernetes clusters</li></ul>"
            ),
        },
        {
            "id": "0cfa89639ce71e3f71966a95f9467973fb1d7618",
            "type": "ebook",
            "name": "Jenkins 2: Up and Running",
            "edition": None,
            "author": "Brent Laster",
            "publisher": "O'Reilly",
            "description": (
                "<p>Design, implement, and execute continuous delivery pipelines with a"
                " level of flexibility, control, and ease of maintenance that was not"
                " possible with Jenkins before. With this practical book, build"
                " administrators, developers, testers, and other professionals will"
                " learn how the features in Jenkins 2 let you define pipelines as code,"
                " leverage integration with other key technologies, and create"
                " automated, reliable pipelines to simplify and accelerate your DevOps"
                " environments.</p><p>Author Brent Laster shows you how Jenkins 2 is"
                " significantly different from the more traditional, web-only versions"
                " of this popular open source automation platform. If you're familiar"
                " with Jenkins and want to take advantage of the new technologies to"
                " transform your legacy pipelines or build new modern, automated"
                " continuous delivery environments, this is your book."
                " </p><ul><li>Create continuous delivery pipelines as code with the"
                " Jenkins domain-specific language</li><li>Get practical guidance on"
                " how to migrate existing jobs and pipelines</li><li>Harness best"
                " practices and new methods for controlling access and"
                " security</li><li>Explore the structure, implementation, and use of"
                " shared pipeline libraries</li><li>Learn the differences between"
                " declarative syntax and scripted syntax</li><li>Leverage new and"
                " existing project types in Jenkins</li><li>Understand and use the new"
                " Blue Ocean graphical interface</li><li>Take advantage of the"
                " capabilities of the underlying OS in your pipeline</li><li>Integrate"
                " analysis tools, artifact management, and containers</li></ul>"
            ),
        },
        {
            "id": "903c02013643cbcd812b618a0e511bece692eb73",
            "type": "ebook",
            "name": "Distributed Systems with Node.js",
            "edition": None,
            "author": "Thomas Hunter",
            "publisher": "O'Reilly",
            "description": (
                "<p>Many companies, from startups to Fortune 500 companies alike, use"
                " Node.js to build performant backend services. And engineers love"
                " Node.js for its approachable API and familiar syntax. Backed by the"
                " world's largest package repository, Node's enterprise foothold is"
                " only expected to grow.</p><p>In this hands-on guide, author Thomas"
                " Hunter II proves that Node.js is just as capable as traditional"
                " enterprise platforms for building services that are observable,"
                " scalable, and resilient. Intermediate to advanced Node.js developers"
                " will find themselves integrating application code with a breadth of"
                " tooling from each layer of a modern service stack.</p><ul><li>Learn"
                " why running redundant copies of the same Node.js service is"
                " necessary</li><li>Know which protocol to choose, depending on the"
                " situation</li><li>Fine-tune your application containers for use in"
                " production</li><li>Track down errors in a distributed setting to"
                " determine which service is at fault </li><li>Simplify app code and"
                " increase performance by offloading work to a reverse"
                " proxy</li><li>Build dashboards to monitor service health and"
                " throughput</li><li>Find out why so many different tools are required"
                " when operating in an enterprise environment</li></ul>"
            ),
        },
        {
            "id": "3c2903318b064108e4cd1e4fa78c974643603546",
            "type": "ebook",
            "name": "Learning Apache OpenWhisk",
            "edition": None,
            "author": "Michele Sciabarrà",
            "publisher": "O'Reilly",
            "description": (
                "<p>Serverless computing greatly simplifies software development. Your"
                " team can focus solely on your application while the cloud provider"
                " manages the servers you need. This practical guide shows you"
                " step-by-step how to build and deploy complex applications in a"
                " flexible multicloud, multilanguage environment using Apache"
                " OpenWhisk. You'll learn how this platform enables you to pursue a"
                " vendor-independent approach using preconfigured containers,"
                " microservices, and Kubernetes as your cloud operating"
                " system.</p><p>Michele Sciabarrà demonstrates how to build a"
                " serverless application using classical design patterns and the"
                " programming language or languages that best fit your task. You'll"
                " start by building a simple serverless application hands-on before"
                " diving into the more complex aspects of the OpenWhisk"
                " platform.</p><ul><li>Examine how OpenWhisk's serverless architecture"
                " works, including the use of packages, actions, sequences, triggers,"
                " rules, and feeds</li><li>Learn how OpenWhisk compares to existing"
                " architectures, such as Java Enterprise Edition</li><li>Manipulate"
                " OpenWhisk features using the command-line interface or a JavaScript"
                " API</li><li>Design applications using common Gang of Four design"
                " patterns</li><li>Use architectural design patterns such as"
                " model-view-controller to combine several OpenWhisk"
                " actions</li><li>Learn how to test and debug your code in a serverless"
                " environment</li></ul>"
            ),
        },
        {
            "id": "db7196a960019ba7250090e87e6eff098ca638c3",
            "type": "ebook",
            "name": "Learning Helm",
            "edition": None,
            "author": "Matt Butcher, Matt Farina, Josh Dolitsky",
            "publisher": "O'Reilly",
            "description": (
                "<p>Get up to speed with Helm, the preeminent package manager for the"
                " Kubernetes container orchestration system. This practical guide shows"
                " you how to efficiently create, install, and manage the applications"
                " running inside your containers. Helm maintainers Matt Butcher, Matt"
                " Farina, and Josh Dolitsky explain how this package manager fits into"
                " the Kubernetes ecosystem and provide an inside look at Helm's design"
                " and best practices.</p><p>More than 70% of the organizations that"
                " work with Kubernetes use Helm today. While the Helm community"
                " provides thousands of packages, or charts, to help you get started,"
                " this book walks developers and DevOps engineers through the process"
                " of creating custom charts to package applications. If you have a"
                " working understanding of Kubernetes, you're ready to"
                " go.</p><ul><li>Explore primary features including frequently used"
                " Helm commands</li><li>Learn how to build and deploy Helm charts from"
                " scratch</li><li>Use Helm to manage complexity and achieve repeatable"
                " deployments</li><li>Package an application and its dependencies for"
                " easy installation</li><li>Manage the entire lifecycle of applications"
                " on Kubernetes</li><li>Explore ways to extend Helm to add features and"
                " functionality</li><li>Learn features for testing, handling"
                " dependencies, and providing security</li></ul>"
            ),
        },
        {
            "id": "99cd8288e400c1e8a6bfa9c3e89eb9cf6bf27fe2",
            "type": "ebook",
            "name": "Dynamic Reteaming, 2nd Edition",
            "edition": None,
            "author": "Heidi Helfand",
            "publisher": "O'Reilly",
            "description": (
                "<p>Your team will change whether you like it or not. People will come"
                " and go. Your company might double in size or even be acquired. In"
                " this practical book, author Heidi Helfand shares techniques for"
                " reteaming effectively. Engineering leaders will learn how to catalyze"
                " team change to reduce the risk of attrition, learning and career"
                " stagnation, and the development of knowledge silos.</p><p>Based on"
                " research into well-known software companies, the patterns in this"
                " book help CTOs and team managers effectively integrate new hires into"
                " an existing team, manage a team that has lost members, or deal with"
                " unexpected change. You'll learn how to isolate teams for focused"
                " innovation, rotate team members for knowledge sharing, break through"
                " organizational apathy, and more.</p><p>You'll"
                " explore:</p><ul><li>Real-world examples that demonstrate why and how"
                " organizations reteam</li><li>Five reteaming patterns: One by One,"
                " Grow and Split, Isolation, Merging, and Switching</li><li>Tactics to"
                " help you master dynamic reteaming in your company</li><li>Stories"
                " that demonstrate problems caused by reteaming anti-patterns</li></ul>"
            ),
        },
        {
            "id": "952c0c6292388cc32251a576357b1c0ec38ac828",
            "type": "game",
            "name": "Ticket to Ride",
            "edition": None,
            "author": "Days of Wonder",
            "publisher": "",
            "description": (
                "<p>The official adaptation of Days of Wonder's best-selling train"
                " board game, Ticket to Ride!<br>In addition to the exciting"
                " multiplayer mode, players will enjoy a new intuitive user interface,"
                " new social media capabilities to share exciting moments, and play"
                " against live opponents from all around the world on the various"
                " boards!</p>\n<p>Ticket to Ride includes: <br>- Alan R. Moon's"
                " official Ticket to Ride USA map with original artwork in full high"
                " resolution<br>- 6 additional maps and 2 mini-expansions (containing 3"
                " variants each) available in the shop in-game, with their own"
                " specificities. Content is added regularly!<br>- Solo play against up"
                " to 4 AI players.<br>- Online Play (WiFi, 3G, 4G) against other"
                " tablets and smartphones (including Android and others), Linux, Mac"
                " and PC gamers. <br>- Pass-and-Play with up to 4 live opponents.<br>-"
                " Online and offline Hall of Fame.</p>"
            ),
        },
        {
            "id": "e7620b58e19a2a47ea812724c94cc4b364f0ffa0",
            "type": "game",
            "name": "Ticket to Ride - Switzerland",
            "edition": None,
            "author": "Days of Wonder",
            "publisher": "Asmodee Digital",
            "description": (
                "<p>Unlike all our other maps, the Swiss map was initially designed as"
                " an Online map, and only later released as an add-on to the board game"
                " version. Specially conceived for 2 and 3 player games, this map is"
                " board game designer Alan R. Moon&rsquo;s"
                " favorite!</p>\n<p><strong>Key Features:</strong></p>\n<ul>\n<li>A"
                " whole new map of Switzerland, designed for 2 and 3"
                " players</li>\n<li>New country tickets linking countries to countries"
                " and cities to neighboring countries</li>\n<li>New locomotive cards"
                " that only work in Tunnels</li>\n<li>Only 40 trains per player &ndash;"
                " use them wisely!</li>\n</ul>\n<p>&nbsp;</p>\n<p><em>Copyright"
                " &copy;2004-2016 Days of Wonder Inc.</em></p>"
            ),
        },
        {
            "id": "40626e64d3ef44153a57182897ddd4dec4c04ed1",
            "type": "game",
            "name": "The Lord of the Rings: Adventure Card Game – Definitive Edition",
            "edition": None,
            "author": "Fantasy Flight Interactive",
            "publisher": "Asmodee Digital",
            "description": (
                "\xa0<i>The Lord of the Rings: Adventure Card Game</i> - Definitive"
                " Edition includes: <br><br>- Two additional campaigns: The Shadow’s"
                " Fall & The Witch-King’s Grasp and their respective heroes. <br>- A"
                " brand new mode: the Mirror of Galadriel which lets you test your deck"
                " in randomly generated quests. <br>- <i>The Lord of the Rings:"
                " Adventure Card Game</i>'s current owners will get the Definitive"
                ' Edition for free." \xa0<br><br>Build a deck of iconic heroes and'
                " challenge the forces of Sauron in this thrilling tactical card game."
                " Travel through famous locations, complete story-driven quests and"
                " forge a new legend of Middle-earth on your own or with a friend in"
                " cooperative mode. But beware: the Eye of Sauron is searching for you."
                " If you draw his attention, all will be lost... \xa0<br><br>Answer the"
                " call of untold adventures, face the dark forces of Sauron and protect"
                " the Free Peoples of Middle-earth. Allies will gather, foes will arise"
                " and so your journey begins. <br><br>The time has come for you to form"
                " and lead your own fellowship of heroes through three immersive"
                " story-driven campaigns, each with its own unique narrative and"
                " challenges. <br><br>Pick three heroes from some of the most"
                " emblematic characters of Middle-earth and build your deck around"
                " their specific abilities and powers. Each Hero has one of four"
                " spheres of influence, Leadership, Lore, Spirit, or Tactics, allowing"
                " you to play specific reinforcement cards while in-game. Choose wisely"
                " when building your deck and make the most of each of your heroes to"
                " get an edge over your opponents during the immersive campaigns. Set"
                " in famous locations across Middle-earth, you will enjoy hours of"
                " gameplay and choices to write your own adventure that will be sung"
                " for ages to come. <br><br>While your journeys may contain great"
                " challenges, taking advantage of your heroes and decks will earn you"
                " victory in battle. Sometimes combining the strength of multiple"
                " champions from the same Sphere of Influence to increase its power can"
                " help you overcome the swarms of enemies that you will face. You might"
                " need to rely on your heroes’ Willpower to increase your Fate Pool and"
                " trigger powerful abilities that can turn the tide of battle. There"
                " are many ways to win, you must find the deck and strategy that works"
                " for your fellowship! <br><br>Every quest will require you to"
                " experiment with strategies as you confront more and more terrifying"
                " foes, ranging from Giant Spiders to powerful dragons, even hordes of"
                " powerful Orcs!"
            ),
        },
        {
            "id": "ef0ee3a228157c39deb731260f39b80c12bcc0a1",
            "type": "game",
            "name": "Ticket to Ride - United Kingdom",
            "edition": None,
            "author": "Days of Wonder",
            "publisher": "Asmodee Digital",
            "description": (
                "Discover the brand-new Ticket to Ride map, the United Kingdom, and the"
                " addition of a new game mechanic, technology! Relive the history of"
                " the railway!<strong>Features :</strong><br><ul"
                ' class="bb_ul"><li>Special rules for locomotives.<br/></li><li>11 new'
                " technology cards to improve your wagons and 5 others to go even"
                " further.<br/></li><li>Develop technologies to create routes with more"
                " than two wagons in England.<br/></li><li>Create a special route"
                " between New York and Southampton that doesn't need any technology"
                " cards</li></ul>"
            ),
        },
        {
            "id": "01c7bc1463dcaed9076ce23ad78c6c1146dce5d3",
            "type": "game",
            "name": "Pandemic: The Board Game",
            "edition": None,
            "author": "Asmodee Digital",
            "publisher": "Z-Man Games",
            "description": (
                "As skilled members of a disease-fighting team, you must keep four"
                " deadly diseases at bay while discovering their cures. Travel the"
                " world, treat infections, and find cures. <br>You must work as a team"
                " to succeed. The clock is ticking as outbreaks and epidemics fuel the"
                " spreading plagues. Can you find all four cures in time? The fate of"
                " humanity is in your hands!<br><br><em>Pandemic: The Board Game</em>"
                " is a family-friendly cooperative game. Simple to understand and lots"
                " of fun, <em>Pandemic: The Board Game</em> puts you in an apocalyptic"
                " situation where you must work as a team to save the"
                " world.<br><br><strong>How to Play</strong><br>In <em>Pandemic: The"
                " Board Game</em> each player has a unique role with different"
                " abilities. On a turn, players will have four actions in order to cure"
                " diseases and save the world. They can remove disease cubes from the"
                " board; fly to a city in need; trade cards with fellow players; and"
                " much more. <br><br>At the end of every player’s turn, new cities are"
                " infected with disease cubes and Epidemics may arise. You must fight"
                " to prevent the outbreaks before they spin out of control.<br><br>In"
                " <em>Pandemic: The Board Game</em>, there is only one way to win: cure"
                " all four diseases before you run out of time! <br><br>An award-wining"
                " board game and player favorite since its release in"
                ' 2008.<br><br><strong>Features</strong><br>\n<ul class="bb_ul">\n<li>7'
                " Role Cards With Unique Abilities</li>\n<li>Supports games for 2, 3,"
                " or 4 players, but can be played solo if you play multiple"
                " roles</li>\n<li>Pass-and-play multiplayer (2-4)</li>\n<li>Three"
                " difficulty settings make the game suitable for beginners,"
                " intermediate players, and experts</li>\n<li>Fully guided interactive"
                " tutorial; plus “Info Mode” for in-game reminders of the"
                " rules</li>\n<li>Full rulebook included for easy access and detailed"
                " reference at all times</li>\n<li>Animated interface gives clear"
                " indication of the game's progress and hotspots</li>\n<li>“Undo”"
                " system</li>\n<li>Adaptive soundtrack</li>\n<li>Complete"
                " implementation of the board game suitable for expert"
                " play</li>\n<li>Interface designed and tested for"
                " ease-of-use</li>\n<li>Supports"
                " multitasking</li>\n</ul>\n<strong>Comments?</strong><br>We want to"
                " know what you think. Please send your feedback, ideas, and comments"
                " about the <em>Pandemic: The Board Game</em> app."
            ),
        },
        {
            "id": "5d11aa5f10901543681b6908347dafb41606d9bb",
            "type": "game",
            "name": "Small World - Cursed",
            "edition": None,
            "author": "Days of Wonder",
            "publisher": "Asmodee",
            "description": (
                "<html>\n <head>\n </head>\n <body>\n  <i>\n   Put a curse on your"
                " Small World!\n  </i>\n  <br>\n  This expansion features winning"
                " contest entries from Gustav Åkerfelt, Philip Harding, Jörg Krismann,"
                " Travis Lauro, Paolo Mori, Leif Steiestol and Daniel Zielinski.\n "
                " <br>\n  <br>\n  Contains\n  <br>\n  <ul>\n   <li>\n    2 new Race"
                " banners and tokens (Kobolds & Goblins)\n    <br>\n   </li>\n   <li>\n"
                "    5 new Special Power badges (Cursed, Hordes of, Marauding,"
                " Ransacking & Were-)\n   </li>\n  </ul>\n  <br>\n  Hit a man while"
                " he's down -\n  <strong>\n   Goblins\n  </strong>\n  conquer In"
                " Decline regions at one less cost...\n  <br>\n  <br>\n  <strong>\n  "
                " Kobolds\n  </strong>\n  aren't necessarily cowards... They just like"
                " to work in teams. It takes 2 Kobolds to occupy a region after you've"
                " conquered it...\n  <br>\n  <br>\n  Your people are now\n  <strong>\n "
                "  Cursed!\n  </strong>\n  Skip over this Special Power and you'll have"
                " to pay 3 coins, not the 1 that is usual...\n  <br>\n  <br>\n  The"
                " only thing better than conquering is\n  <strong>\n   Ransacking\n "
                " </strong>\n  . Take 1 coin away from an opponent for every territory"
                " you conquer...\n  <br>\n  <br>\n  The Hordes are at the door. Add the"
                " 2\n  <strong>\n   Hordes of\n  </strong>\n  tokens to increase the"
                " size of your active Race...\n  <br>\n  <br>\n  The moon is full and"
                " the Were-people are howling. At night (even-numbered turns) the\n "
                " <strong>\n   Were-\n  </strong>\n  power lets you conquer all regions"
                " with 2 less tokens than normal...\n  <br>\n  <br>\n  It's time for"
                " Double-Jeopardy! After an initial attack,\n  <strong>\n   Marauding\n"
                "  </strong>\n  forces get a second chance each turn to conquer even"
                " more territory...\n </body>\n</html>"
            ),
        },
        {
            "id": "121816bcf493ebf1980de79acde0351de80165de",
            "type": "game",
            "name": "Small World",
            "edition": None,
            "author": "Days of Wonder",
            "publisher": "Asmodee Digital",
            "description": (
                '<strong class="hmb">CONTROL FANTASY RACES, SET OFF TO CONQUER NEW'
                " LANDS, OVERTHROW YOUR ENEMIES AND CLAIM THE VICTORY! </strong>"
                " <br><br>In this digital adaptation of the legendary board game, dive"
                " into a world inhabited by whimsical fantasy races. <br><br>Take"
                " control of the dwarfs, wizards, amazons, giants, orcs or even humans."
                " Then send out your troops to battle mercilessly and conquer new"
                " regions. Make shrewd use of the special powers of your races to"
                " expand your empire and win the game! Meanwhile, weaker civilizations"
                " will be ruthlessly chased out of this <i>Small World</i>! Carve out"
                " your place in a world that’s too small to accommodate"
                " everyone!<br><br>This game of strategy and conquest can be played"
                " over and over again thanks to the nearly endless combinations of"
                " races and special powers. Whether you’re a newbie or an experienced"
                " player, you’ll love playing this classic board game with simple rules"
                " and tactical gameplay."
            ),
        },
        {
            "id": "992500244ab556e4b146f6ef5e9f5e7feb9f89ce",
            "type": "game",
            "name": "A Game of Thrones: The Board Game - Digital Edition",
            "edition": None,
            "author": "Dire Wolf",
            "publisher": "Asmodee Digital",
            "description": (
                '"A must-buy for any Game of Thrones gamers or fans. Excellent'
                ' all-around."<br>4.5/5 - Hey Poor Player<br><br><strong>A Game of'
                " Thrones: The Board Game – Digital Edition</strong><span>&nbsp;is the"
                " digital adaptation of the top-selling strategy board game from"
                " Fantasy Flight Games. During the game, players spread their influence"
                " across Westeros through a combination of strategic planning,"
                " masterful diplomacy, and military might. As one of the Great Houses,"
                " will you conquer with force, forge alliances, rally your townsfolk,"
                " or cunningly coerce your way to the Iron"
                " Throne?<br></span><br><span>Based on the best-selling A Song of Ice"
                " and Fire series of fantasy novels by George R.R. Martin, A Game of"
                " Thrones: The Board Game – Digital Edition allows up to six players to"
                " play online, or a single player with up to five AI opponents to play"
                " locally. The game is set after the death of King Robert Baratheon and"
                " allows each player to assume the role of one of the Great Houses of"
                " the Seven Kingdoms in an attempt to assault King’s Landing and claim"
                " the Iron Throne.</span><br><br><span>To be declared ruler of the"
                " Seven Kingdoms, you have 10 rounds to use diplomacy and warfare to"
                " your advantage to control as many strategic areas of the"
                " map.</span><br><span>Conquer with care as your resources are scarce"
                " and your troops are not expendable. Muster your army, plan your"
                " orders wisely and seize strategical lands with your Footmen, Knights,"
                " Siege Engine and ships.</span><br><span>During the turmoil of a"
                " battle, use well-known characters from your house to take the upper"
                " hand and vanquish your enemies.</span><br><br><strong>A Game of"
                " Thrones: The Board Game – Digital Edition</strong><span>&nbsp;is a"
                " game of negotiation and deception.</span><br><span>Each round, you"
                " secretly assign one order token to each of your armies: promise"
                " support, offer peace, forge alliances, betray a vulnerable ally - a"
                " House that dares set its eyes on the Iron Throne must turn many"
                " wheels within wheels to achieve its ends.</span><br><br><span>Move up"
                " the three influence tracks by betting your hard-earned power tokens."
                " Obtain the Iron Throne, the Messenger Raven and the Valyrian steel"
                " tokens, each granting you strategic and social gameplay advantages to"
                " hold sway over rival houses.</span><br><span>However, keep an eye"
                " beyond the Wall as an army of barbaric wildlings gather to descend"
                " upon the continent! All houses must cooperate to gather enough power"
                " tokens to reinforce the Night’s Watch and fend off the wildlings, or"
                " the consequences could be devastating…</span>"
            ),
        },
        {
            "id": "3a9ef71c395135f24c05d740aba5e660dd6408fa",
            "type": "game",
            "name": "Carcassonne - Tiles & Tactics",
            "edition": None,
            "author": "Asmodee Digital",
            "publisher": "",
            "description": (
                "New version of the muti-awarded game. Now in 3D. Includes improved IA,"
                " 3D landscape, new exclusive features. <br><br>*** Carcassonne fits"
                " that opening game niche that every game group needs. -Tyler Nichols,"
                " Board Game Quest<br>*** Carcassonne = Great game, great mechanics,"
                " great pieces, great fun! -The Board Game Family<br>*** Carcassonne's"
                " recent Android re-release and its fresh, new features are a joy to"
                " experience*** Pocket Gamer<br><br>A TILE PLACEMENT GAME OF CREATING"
                " LANDSCAPES, CLAIMING AREAS, AND GAINING POINTS<br><br>Carcassonne is"
                " a modern classic tile-placement game based on the award wining game"
                " in which the players draw and place a tile with a piece of southern"
                " French landscape on it. The tile might feature a city, a road, a"
                " cloister, grassland or some combination thereof, and it must be"
                " placed adjacent to tiles that have already been played, in such a way"
                " that cities are connected to cities, roads to roads, et cetera. The"
                " player can then decide to place one of his followers, so called"
                " Meeples, on one of the areas on it: on the city as a knight, on the"
                " road as a robber, on a cloister as a monk, or on the grass as a"
                " farmer. When that area is complete, that meeple scores points for its"
                " owner. Each new game is a new experience thanks to the ever-changing"
                " landscape.<br><br>ENJOY FUN AND TACTICAL GAMEPLAY<br><br>During a"
                ' game of Carcassonne, players are faced with decisions like: "Is it'
                ' really worth putting my last meeple there?" or "Should I use this'
                " tile to expand my city, or should I place it near my opponent"
                " instead, making it harder for him to complete his goal and score"
                ' points?" Since players place only one tile and have the option to'
                " place one meeple on it, turns proceed quickly even if it is a game"
                " full of options and possibilities.<br><br>FEATURES<br>\n<ul>\n<li>Fun"
                " and tactical gameplay adapted from the award-winning Carcassonne"
                " board game</li>\n<li>Solo mode</li>\n<li>Pass &amp; Play on the same"
                " device with your friends and family</li>\n<li>Detection of blocked"
                " locations once the tile is placed.</li>\n<li>Online multiplayer mode"
                " includes:\n<ul>\n<li>Public games to play with players all around the"
                " world</li>\n<li>Private games to invite your friends</li>\n<li>Ranked"
                " games and leaderboards</li>\n<li>Chat &amp;"
                " Lobby</li>\n</ul>\n</li>\n<li>3D modelisation (vs 2D for the previous"
                " versions and the physical game)</li>\n<li>Additional strategic layers"
                " compared to the physical version:\n<ul>\n<li>field view which allows"
                " you to see the field possession of each player</li>\n<li>remaining"
                " tile list: allows you to see the tiles which are remaining in the"
                " draw pile</li>\n</ul>\n</li>\n<li>2D/3D view"
                " swap</li>\n</ul>\n<br>Languages available: English, French, German"
                " Italian, Spanish"
            ),
        },
        {
            "id": "942706a547b46406e27b727f2f9e51685fee5a53",
            "type": "game",
            "name": "Scythe: Digital Edition",
            "edition": None,
            "author": "The Knights of Unity",
            "publisher": "Asmodee Digital",
            "description": (
                "<p>In an alternate reality in 1920s Europa, it's been several years"
                ' since the "Great War", but the ashes of the conflict are still hot'
                " and the war is entering a new phase. The first conflict saw the"
                " emergence of some incredible engines of war known as Mechs. Built by"
                ' "The Factory", an independent city-state which has since become the'
                " object of everyone's desire, these technological monstrosities roam"
                " the snowy landscapes of Europa. <br /><br /> Be the hero of one of"
                " the five factions &ndash; Saxony Empire, Crimean Khanate, Rusviet"
                " Union, Polania Republic or Nordic Kingdom &ndash; and become the"
                " richest and most powerful nation in all of Europa during these dark"
                " times! To assure the victory of your people, you will need to explore"
                " and conquer new territories, enlist new recruits and deploy your"
                " forces by building formidable and terrifying combat Mechs. Replay"
                " history in a fictional past full of mechanical engines and"
                " technology, where each choice you make will be critical. Choose your"
                " battles with care, because in Scythe, victory is achieved with and"
                " for the people!</p>"
            ),
        },
        {
            "id": "dddbb7004e8e1b868389b84b41758251c10ecedb",
            "type": "game",
            "name": "Love Letter",
            "edition": None,
            "author": "Nomad Games",
            "publisher": "Asmodee Digital",
            "description": (
                "DRAW, PLAY AND BLUFF, FOR ONLY ONE SUITOR WILL BE ABLE TO WIN THE"
                " HEART OF THE PRINCESS\n<br>\n<br>\nYou and other suitors are prepared"
                " to do anything to get your <i>love letter</i> to the princess. She's"
                " shut herself inside her palace, so you're forced to use go-betweens"
                " to deliver the message. Guards, princes, the king, the countess..."
                " Who will turn out to be the best ally to help win your beloved's"
                " heart?\n<br>\n<br>\nYou only ever have two cards in your hand. Draw"
                " and play your cards to get closer to the princess. Everyone staying"
                " in the castle could aid you in their own way: guards and princes can"
                " help discredit letters from other suitors, priests will give you"
                " precious information about your rivals while the handmaiden will"
                " protect your letter at any cost!\n<br>\n<br>\nAs the game progresses,"
                " you'll have to think strategically, bluff and try to read your"
                " opponents' game. When the deck is used up, the card in your hand will"
                " be the character holding your letter for the princess. The strongest"
                " card, i.e. the character who's closest to the princess,"
                " wins!\n<br>\nSend the other suitors packing, gain the advantage and"
                ' win the game. Let\'s get started!\n<strong class="hmb">\n <br>\n'
                " <br>\n Features:\n</strong>\n<br>\n<ul>\n <li>\n  Simple rules and"
                " quick turns in this game adapted from the multi-award winning card"
                " game <i>Love Letter</i>\n  <br>\n </li>\n <li>\n  1 to 4 players\n "
                " <br>\n </li>\n <li>\n  Play in single-player mode against the"
                " computer, against your friends in private multiplayer or face suitors"
                " from all over the world in online mode\n  <br>\n </li>\n <li>\n  16"
                " cards representing 8 types of characters found at the Court: Guards,"
                " Priests, Barons, Handmaidens, Princes, King, Countess and of course"
                " the Princess\n </li>\n</ul>\n<br>\n<br>\nAvailable languages: French,"
                " English, Spanish, Italian, German, Japanese, Simplified Chinese,"
                " Russian.\n"
            ),
        },
        {
            "id": "2360cf24b4ae3a579f3d46ce7fee6a171fbeef9c",
            "type": "game",
            "name": "Ticket To Ride - France",
            "edition": None,
            "author": "Days of Wonder",
            "publisher": "Asmodee Digital",
            "description": (
                '<html>\n <head>\n </head>\n <body>\n  <strong class="hmb">\n  '
                " <br>\n   <br>\n   Relive the construction of the first railway lines"
                " in France against a backdrop of impressionism and the Industrial"
                " Revolution.\n  </strong>\n  <br>\n  <br>\n  For years it was only"
                " possible to claim routes… But that's over now! Discover one of the"
                " most strategic cards in Ticket to Ride!\n  <br>\n  <br>\n  <ul>\n  "
                " <li>\n    Start by building your railway and then setting down your"
                " trains\n    <br>\n   </li>\n   <li>\n    Place your rails over"
                " crossings to block the tracks and force your opponents to hit their"
                " brakes\n    <br>\n   </li>\n   <li>\n    New Destinations cards:"
                " build rail tracks all the way to Switzerland, Italy and even"
                " Germany\n    <br>\n   </li>\n   <li>\n    Make sure you don't give"
                " any other players the chance to take control of a route that you've"
                " painstakingly built…\n    <br>\n   </li>\n   <li>\n    Bluff,"
                " deceive, and play your cards right in this expansion which is sure to"
                " shake up your habits.\n   </li>\n  </ul>\n </body>\n</html>"
            ),
        },
        {
            "id": "f8111b710467effa7ae4f365767da9c0a9226dc1",
            "type": "game",
            "name": "Terraforming Mars",
            "edition": None,
            "author": "Asmodee Digital",
            "publisher": "",
            "description": (
                "The taming of the Red Planet has begun! <br>Corporations are competing"
                " to transform Mars into a habitable planet by spending vast resources"
                " and using innovative technology to raise the temperature, create a"
                " breathable atmosphere, and make oceans of water. As terraforming"
                " progresses, more and more people will immigrate from Earth to live on"
                " the Red Planet. <br>In <i>Terraforming Mars</i>, you control a"
                " corporation with a certain profile. Play project cards, build up"
                " production, place your cities and green areas on the map, and race"
                " for milestones and awards! Will your corporation lead the way into"
                ' humanity’s new era? <strong class="hmb"> <br><br>Features: </strong>'
                " <br>\n<ul>\n<li><strong> The official adaptation of the cult board"
                " game, </strong> faithfully developed with the help of Jacob"
                " Fryxelius, author of the board game. </li>\n<li><strong> Turn-based"
                " strategy: </strong> choose a specialized corporation, build"
                " facilities, research innovative technologies and manage your"
                " resources productions </li>\n<li><strong> Life on Mars? </strong>"
                " Improve the conditions on the Red Planet by warming it up to melt the"
                " ice and create oceans, planting oxygen-producing flora and"
                " introducing both small and big animals. </li>\n<li><strong>"
                " Corporation rivalry: </strong> it’s a nice forest you’ve planted"
                " there - wouldn’t it be a shame if a large asteroid was steered to"
                " crash right on it? Develop Projects that will slow down your"
                " opponents! </li>\n<li><strong> Mars for all: </strong> play solo or"
                " with up to 5 players in multiplayer games against local or online"
                " opponents, humans or AI </li>\n<li><strong> Game variant: </strong>"
                " Try the Corporate Era rules, for a more complex game. This variant"
                " adds new cards, including 2 new corporations, and focuses on economy"
                " and technology. These are projects that do not contribute directly to"
                " terraforming, but make the corporations stronger, adding new"
                " strategic choices to the game! </li>\n<li><strong> Solo Challenge:"
                " </strong> Finish <i>terraforming Mars</i> before the end of"
                " generation 14. Try new rules and features in the most challenging"
                " solo mode on the (Red) planet. </li>\n<li><strong> Draft variant"
                " available: </strong> Add a new level of strategy and depth by"
                " choosing your best cards and blocking your opponents. During the"
                " Research Phase, start by drawing 4 cards, choose one and pass the"
                " others to the next player. Continue to choose a card and pass the"
                " rest on until all cards drawn have been drafted. Which card will you"
                " choose? Will you block your opponent from getting a card, or choose"
                " one that fits your strategy best? </li>\n<li><strong> More to"
                " terraform: </strong> additional content to come after"
                " launch</li>\n</ul>"
            ),
        },
        {
            "id": "ade4112bdfbfb80278f3ba4d1e118ca521033de2",
            "type": "game",
            "name": "Ticket to Ride - USA 1910",
            "edition": None,
            "author": "Days of Wonder",
            "publisher": "",
            "description": (
                "<p>Expand your base game with 3 new Game variants and a whole new deck"
                " of Destinations tickets! Includes 35 new Destination Tickets and a"
                " new GlobeTrotter bonus card for completing the most tickets. There"
                " are three new ways to play: the 1910 variant, using only the new"
                " Destination Tickets; the Mega Game variant, featuring all tickets;"
                " and the Big Cities variant, with select large cities"
                " tickets.</p>\n<p><strong>Key Features:</strong></p>\n<ul>\n<li>3 new"
                " ways to play the original US Map</li>\n<li>1910 variant features 35"
                " whole new Destination Tickets</li>\n<li>Mega Game features a huge"
                " deck of 69 Destination Tickets!</li>\n<li>Big Cities variant"
                " exclusively features Tickets to major US cities</li>\n<li>New"
                " GlobeTrotter Bonus for most tickets"
                " completed</li>\n</ul>\n<p>&nbsp;</p>\n<p><em>Copyright"
                " &copy;2004-2016 Days of Wonder Inc.</em></p>"
            ),
        },
        {
            "id": "83e7cbebaceda94feaedbbf7f931ccddc4bb4e17",
            "type": "game",
            "name": "Ticket to Ride - Legendary Asia",
            "edition": None,
            "author": "Days of Wonder",
            "publisher": "Asmodee Digital",
            "description": (
                "Travel along the Silk Road and wind your way through the hustle and"
                " bustle of Indochina in this new map of Ticket to Ride Legendary Asia!"
                " Just be ready for a hair-rising ride as you venture through the"
                " Mountain passes of the Himalayas in François Valentyne's winning"
                " entry to the Ticket to Ride 2011 Map Design"
                " Contest!<br><br><strong>Key Features:</strong><br>\n<ul"
                ' class="bb_ul">\n<li>A whole new map of Legendary Asia, from Samarkand'
                " to Rangoon and beyond</li>\n<li>New Mountain Routes, that use up your"
                " trains but grant you an immediate bonus</li>\n<li>The new Mountain"
                " Routes can considerably impact the length of your game - Watch"
                " out!</li>\n<li>A new Mongolian Horse marker to keep track of game"
                " turns played </li>\n<li>A new Asian Explorer bonus for connecting the"
                " most cities together</li>\n</ul>"
            ),
        },
        {
            "id": "49d0d2f46f185f1f38f0fef1fb9b2a29033e7c48",
            "type": "game",
            "name": "Blood Rage: Digital Edition",
            "edition": None,
            "author": "Exozet",
            "publisher": "Asmodee Digital",
            "description": (
                "<strong>Ragnarök is coming! </strong> The sky is falling and the end"
                " is upon you… <br>In Blood Rage, the digital adaptation of the"
                " <strong> hit strategy board game </strong> , you <strong> lead a"
                " proud Viking clan </strong> in their <strong> final fight </strong>"
                " for glory and the right of <strong> passage to Valhalla </strong>"
                " before the world finally comes to its fiery conclusion. <br>Take"
                " command of your warriors, pillage villages, make good use of gifts"
                " from the gods and conquer your place with Odin in Valhalla."
                " <br><strong> Life is fleeting, but glory is eternal. Now is the time"
                " for rage!</strong><br><br>Created by acclaimed designer Eric Lang"
                " (Rising Sun, Arcadia Quest, Chaos in the Old World), Blood Rage lets"
                " you <strong> lead one of the seven ancient Viking clans </strong> :"
                " The Wolf, Bear, Serpent, Raven, Ram, Wild Boar and Stag clan."
                " <strong> Each with their own unique miniatures </strong> of warriors"
                " and leaders. <br>In Blood Rage, your <strong> goal is to achieve the"
                " greatest amount of glory </strong> before the end of the third and"
                " final age—and the arrival of Ragnarök.<br><br>Each god is generous in"
                " their own way: Frigga provides resources and support, Tyr strengthens"
                " your clan in battle while Loki rewards losing battles or punishes the"
                " opposing winner. <br><br><strong> Drafting gifts </strong> from a god"
                " will determine the strategy you want to implement. Choose your cards"
                " wisely or deprive your opponents of precious gifts. <br><br>For your"
                " clan, there are <strong> many paths to Glory </strong> : <br>•"
                " <strong> Invade </strong> the mythical land of Midgard and its nine"
                " provinces, pillaging their villages and the province of Yggdrasil."
                " <br>• <strong> Crush </strong> other clans in ferocious battles and"
                " encounter legendary creatures from Norse mythology. <br>• <strong>"
                " Fulfill </strong> quests in honor of the mighty gods. <br>• <strong>"
                " Die </strong> gloriously in battle or from Ragnarök as any Viking was"
                " born to do. <br>• The <strong> only losing strategy </strong> in"
                " Blood Rage is to <strong> cower from combat </strong> ."
                " <br><br>Earning your place to Valhalla in single-player mode is"
                " glorious. Eternal triumph, however, can only be achieved by reaching"
                " the top of the leaderboard in <strong> ranked online multiplayer"
                " </strong> . <br><br><br>\n<ul>\n<li><strong> Fight to gain entry to"
                " Valhalla </strong> : Pillage, fight, sacrifice… Experience a new type"
                " of strategy game where victory can only be achieved by commanding"
                " your warriors in the field of battle in the face of final"
                " doom.</li>\n<li><strong> Welcome to Midgard </strong> : Dozens of 3d"
                " scanned miniatures and a dynamic board faithful to the original"
                " boardgame.</li>\n<li><strong> Multi-layered strategy game </strong> :"
                " Blood Rage mixes draft, hidden cards, resource management and its"
                " sheer load of trickery. Plan your strategy but be ready to adapt to"
                " your opponents’ choices: winning battles is not always the best"
                " course of action.</li>\n<li><strong> Up to five Players </strong> :"
                " Introducing the ‘5th player expansion’ giving the options to play up"
                " to five players. All the miniatures from the Ram, Wild Boar and Stag"
                " clans as well as the God Gifts cards from the ‘5th Player Expansion’"
                " of the board game are available in this digital edition for"
                " free.</li>\n<li><strong> Become the greatest Viking Leader </strong>"
                " : Play solo against AI, local multi-player via hotseat or online"
                " multiplayer with ELO ranking and leaderboards.</li>\n</ul>\n<video"
                ' autoplay="autoplay" loop="loop" muted="muted" preload="auto"'
                ' style="width: 616px; height: 347px;">\n   <source'
                ' src="https://hb.imgix.net/2127cb927c5f2a2c589313dc058c101b9d78697f.gif?auto=format&amp;fm=mp4&amp;s=838b106dc04003a2ab4d9352cb3a1005"'  # noqa: B950
                ' type="video/mp4">\n   \n  </video>'
            ),
        },
        {
            "id": "2147be5c48f4c153ab7541776a60af5776b3a484",
            "type": "game",
            "name": "Small World - Royal Bonus",
            "edition": None,
            "author": "Days of Wonder",
            "publisher": "Asmodee Digital",
            "description": (
                "Add a little treachery to your game with the ruthless characters in"
                " this mini expansion! Try out new playing styles that wisely harness"
                " the special powers of each race.<br><br>Carve out your place in a"
                " world that’s too small to accommodate everyone!<br><br>This"
                " SmallWorld mini expansion includes three new Races (Fauns, Igors and"
                " Sylphs) and three Special Powers (Aquatic, Fireball and Behemoth)."
            ),
        },
        {
            "id": "5aa38aae192646897a15d385eacff126b9ae7003",
            "type": "game",
            "name": "Arkham Horror: Mother's Embrace",
            "edition": None,
            "author": "Asmodee Digital",
            "publisher": "",
            "description": (
                "Inspired by the award-winning board game franchise,\xa0Arkham Horror:"
                " Mother’s Embrace\xa0is an investigation game served with turn-based"
                " combat, set in the haunted worlds of H.P. Lovecraft’s Cthulhu mythos."
                " Plunge into an original story written by Fantasy Flight Interactive’s"
                " official writers and explore the\xa0American Roaring Twenties."
                " <br><br>The year is 1926: a professor of astronomy is found dead in"
                " her mansion and everything indicates that she has been the victim of"
                " a heinous murder. Choose from 12 intrepid investigators from the"
                " Arkham Horror games, each with a unique set of skills,"
                " and\xa0assemble your team to shed the light over this mysterious"
                " death. <br><br>Find clues, perform interrogations and"
                " progress\xa0through nine chapters\xa0as the story unfolds. Your"
                " investigation will take you to visit\xa0shadowed institutions and"
                " mysterious locales, ranging from Miskatonic University, the Arkham"
                " Asylum, and the bayous of Louisiana. <br><br>As the investigators get"
                " closer to their goal, your squad will have to face\xa0curious"
                " science, living nightmares, and a sinister cult, whose mad scheme is"
                " to bring about the end of everything. Use a large variety of melee"
                " and ranged weapons, as well as powerful items and devastating magic"
                " spells to defeat your\xa0opponents in turn-based combat; while you"
                " attempt to retain your sanity. <br><br>As you face off"
                " against\xa0Lovecraftian horrors, your investigators will descend"
                " deeper into the depths of madness,\xa0affecting their level of sanity"
                " and causing traumas that will impact the course of your"
                " investigation. Care about your sanity and make the right choices… the"
                " Ancient Ones are preparing their return."
            ),
        },
        {
            "id": "c01a3eb93fcd79fed7b4021b7d3ce8e2782b69ac",
            "type": "game",
            "name": "Ticket to Ride - Nordic Countries",
            "edition": None,
            "author": "Days of Wonder",
            "publisher": "",
            "description": (
                "<p>This new challenging vertical map will make you cross European"
                " Nordic Countries. From Copenhagen in Denmark to Helsinki in Finland,"
                " discover the snowy landscape by crossing Norway and Sweden. Succeed"
                " in building one of the biggest paths in the app. With this brand new"
                " vertical and competitive map, <em>Ticket to Ride</em> makes you cross"
                " the great countries of Northern Europe. Go from Copenhagen, Denmark"
                " to Helsinki, Finland through the snowy territories of Sweden and"
                " Norway.</p>\n<p>Faithful to the board game&rsquo;s expansion, this"
                " new map introduces specific and exciting"
                " rules:</p>\n<ul>\n<li>Locomotives can&rsquo;t be used as wild cards"
                " to claim regular routes anymore: they can only be used on tunnels and"
                " ferries.</li>\n<li>If you are missing a locomotive to claim a ferry"
                " route, you can replace it with any three cards of any"
                " color.</li>\n<li>Finally, one of the routes will be particularly"
                " difficult to own, as it will require 9 train cars to be acquired,"
                " which is the longest Ticket to Ride ever had so far. Its other"
                " characteristic is that even if you don&rsquo;t have 9 cards of the"
                " same color, you can fill any missing train car with any 4 cards of"
                " other colors.</li>\n</ul>\n<p>The Nordic Countries vertical map"
                " promises high tension games and fierce battles to be the first to own"
                " the routes essential to your strategy. Will you be ingenious enough"
                " to become the greatest railway company of Nordic"
                " Countries</p>\n<p>&nbsp;</p>\n<p><em>Copyright &copy;2002-2016 Days"
                " of Wonder Inc.</em></p>"
            ),
        },
        {
            "id": "c54096ef3279d9728f48053adda78be77ac4adc7",
            "type": "game",
            "name": "Pandemic - On the Brink: Mutation",
            "edition": None,
            "author": "Asmodee Digital",
            "publisher": "Z-Man Games",
            "description": (
                'You thought you saved humanity already? "On the Brink: Mutation" DLC'
                " brings a fifth, special, highly dangerous and purple, disease to"
                " eradicate.\n<br>\n<br>\nDuring infections, the Mutation will pop up"
                " unpredictably and becomes a new disease to fight in contaminated"
                " cities. Making the game more challenging than ever before, this"
                " disease divides the team’s efforts and will cost them precious"
                " time.\n<br>\n<br>\nYou’ll need to plan ahead and coordinate the whole"
                " team to fight the new virus and find a cure for the 5th disease.\n"
            ),
        },
        {
            "id": "985aeb366fc1cbe42e1c149dcbd898c509127518",
            "type": "game",
            "name": "Ticket to Ride - India",
            "edition": None,
            "author": "Days of Wonder",
            "publisher": "Asmodee Digital",
            "description": (
                "Embark on a tour of Ian Vincent's <i>India</i> and discover one of the"
                " most densely populated and colorful countries of the world. The year"
                " is 1911, and the world is changing fast in the British Raj. Will you"
                " complete your Grand Tour in time, or lose to more cunning – or simply"
                " better connected – opponents?<br/><br/>Ticket to Ride now supports"
                " vertical maps! The map India is the first vertical map made"
                " available. This vertical map brings a new way of playing by"
                " introducing loops called mandalas. On this map players who decide to"
                " reach two cities through mandalas i.e. connecting two cities"
                " following loops will get more points."
            ),
        },
        {
            "id": "f85fc7beb29819b3df6586b35036a8bbea8fd1ac",
            "type": "game",
            "name": "Splendor",
            "edition": None,
            "author": "Days of Wonder",
            "publisher": "Asmodee Digital",
            "description": (
                "<p>The OFFICIAL digital adaptation of the best-selling board game"
                " Splendor.<br>In Splendor, you embody a rich merchant during the"
                " Renaissance. You will use your resources to acquire mines,"
                " transportation methods and artisans who will allow you to turn raw"
                " gems into beautiful jewels, attract nobles and earn"
                " prestige.</p>\n<p>The digital version of Splendor faithfully adapts"
                " all the various elements of the Space Cowboys’ award-winning board"
                " game:<br>- Fast and easy to learn, yet hard to master.<br>- Lavish"
                " graphics and cards, true to the original game.<br>- Solo mode, pass"
                " &amp; play and online multiplayer (2 to 4 players).<br>- An exclusive"
                " game mode: scenario-based “Challenges”.<br>- Multiple types of"
                " Artificial Intelligence, based on unique strategy behaviors instead"
                " of difficulty.<br>- Achievements board.<br>- Worldwide leaderboards"
                " and rank system by connecting with a Days of Wonder"
                " account.<br><br>Check out all the system requirements&nbsp;<a"
                ' href="https://support.humblebundle.com/hc/en-us/articles/231780448"'
                ' target="_blank" rel="noopener">here</a>.</p>'
            ),
        },
        {
            "id": "e9771c6e9f2cb38f4be73b7fd6efc8bd38a7bf28",
            "type": "game",
            "name": "Small World - A Spider's Web",
            "edition": None,
            "author": "Days of Wonder",
            "publisher": "Asmodee Digital",
            "description": (
                '<p>This Small World "A Spider\'s Web" mini expansion'
                " contains:<br><br>• 3 new Races (Ice Witches, Slingmen and Skags)"
                " <br>• 3 Special Powers (Lava, Copycat and Soul-Touch).<br><br>Carve"
                " out your place in a world that is too small to accommodate"
                " everyone!</p>"
            ),
        },
        {
            "id": "55b443f7b41a40e0fde403ec6b1d13932e1f0813",
            "type": "game",
            "name": "Ticket to Ride - Europe",
            "edition": None,
            "author": "Days of Wonder",
            "publisher": "Asmodee Digital",
            "description": (
                "<p><strong><em>Ticket to Ride Europe&nbsp;</em></strong><strong>also"
                " includes the mini expansion&nbsp;</strong><strong><em>Europa"
                " 1912.</em></strong><br /><br />Ticket<em> to Ride Europe</em> takes"
                " you on a new train adventure through the great cities of"
                " turn-of-the-century Europe. Discover new rules like Tunnels, Ferries"
                " and Stations in this new map, our most popular add-on for <em>Ticket"
                " to Ride</em>!</p>\n<p><strong>Key"
                " Features:</strong></p>\n<ul>\n<ul>\n<li>A whole new map of Europe,"
                " requiring you to adapt your strategies</li>\n<li>New Train Stations,"
                " that let you borrow Routes from opponents</li>\n<li>New Ferry routes"
                " that go over water, using locomotives</li>\n<li>New Tunnels, so dark"
                " you&rsquo;re never quite sure how long they&rsquo;ll be</li>\n<li>A"
                " deck of Tickets, including Long and Short routes</li>\n<li>A new"
                " bonus for the most Tickets"
                " completed</li>\n</ul>\n</ul>\n<p>&nbsp;</p>\n<p><em>Copyright"
                " &copy;2004-2016 Days of Wonder Inc.</em></p>"
            ),
        },
        {
            "id": "82f7c5a365fa929262a37d5a9ef95fa839a0e5d6",
            "type": "game",
            "name": "Pandemic: On the Brink - Roles & Events",
            "edition": None,
            "author": "Asmodee Digital",
            "publisher": "",
            "description": (
                "With humanity on the brink of extinction, you’ll have to recruit an"
                " elite team of specialists to eradicate the diseases spreading across"
                " the globe. Pick from 6 brand new roles to assemble the best"
                " team.\n<br>\n<br>\nIncrease your actions with the Generalist, keep a"
                " disease crisis under control with the Containment Specialist, or"
                " gather extra knowledge with the Archivist. The Field Operative and"
                " Troubleshooter will help you stay one step ahead, while the"
                " Epidemiologist’s special skill will help with your research for the"
                " cures.\n<br>\n<br>\nIn addition to the 6 new roles, there are also 8"
                " new event cards for even more variety. If finding cures is becoming"
                " routine on the Heroic difficulty, tackle a new challenge at the"
                " Legendary level!\n"
            ),
        },
        {
            "id": "f652de40f1b56ba33de4ce2464c58650c98fda1b",
            "type": "software",
            "name": "Angular for Beginners - Build a Language-Learning App",
            "edition": '<span class="callout-msrp">MSRP: $50<br></span>Web Development',
            "author": "",
            "publisher": "Zenva",
            "description": (
                "<p>Build powerful, single-page webapps by exploring"
                " Angular!</p><p>Inspired by the Model-View-Controller design pattern,"
                " the open-source, TypeScript-based Angular framework was designed to"
                " separate app logic from the frontend – resulting in cleaner code and"
                " easier rich data injection. You’ll get to explore both the tools and"
                " features of Angular while building a language-learning quiz game"
                " complete with timer and scoring. Not only will this let you enhance"
                " your web development skills, but also prepare you to build"
                " interactive apps usable on mobile and desktop.</p><p><strong>You will"
                " learn how to:</strong></p><ul><li>Set up an Angular"
                " project</li><li>Utilize Components to control app"
                " elements</li><li>Style webapps with Bootstrap and CSS</li><li>Bind"
                " backend data with frontend rendering</li><li>Detect user"
                " interaction</li><li>Add game logic like timers and"
                " scoring\xa0</li></ul><p>… and more!</p>"
            ),
        },
        {
            "id": "225ad9927446a52f1efded897ffb81b5b718906d",
            "type": "software",
            "name": "HTML Foundations",
            "edition": '<span class="callout-msrp">MSRP: $50<br></span>Web Development',
            "author": "",
            "publisher": "Zenva",
            "description": (
                "<p>Build websites and more by learning the foundation for all web"
                " development – HTML.</p><p>HTML dictates the structure and base"
                " appearance of every webpage. Not only is it a fundamental starting"
                " point for any developer pursuing web development, but it also plays a"
                " crucial role as you develop your skills further with CSS and"
                " JavaScript.</p><p>In this course, you will develop a strong set of"
                " HTML skills needed to get started on your web development journey, as"
                " you learn both to structure your page, add specific elements, and"
                " even start adding website interactivity.</p><p><strong>You will learn"
                " how to:</strong></p><ul><li>Create your first HTML"
                " file</li><li>Handle text and its various attributes</li><li>Utilize"
                " images, links, lists, tables, and more</li><li>Work with classes and"
                " IDs</li><li>Display HTML elements in various ways</li><li>Deal with"
                " various user inputs</li></ul>"
            ),
        },
        {
            "id": "7a3c6ad97b74f1ebab33db0a183847fd6572df39",
            "type": "software",
            "name": "JavaScript Mini-Projects - Language Learning Game",
            "edition": '<span class="callout-msrp">MSRP: $50<br></span>Web Development',
            "author": "",
            "publisher": "Zenva",
            "description": (
                "<p>Expand your skills with JavaScript by building a browser-based"
                " language learning app!</p><p>With no additional frameworks or"
                " libraries required, you’ll explore the practical applications of"
                " JavaScript by creating a game from scratch. This game will feature"
                " multiple questions, the ability to track player scores for correct"
                " answers, and more using only common JavaScript and coding"
                " fundamentals. You’ll not only learn how to dynamically integrate"
                " JavaScript into your webpages, but also master skills and systems to"
                " create various apps and games for future web-based"
                " projects!</p><p><strong>You will learn how"
                " to:</strong></p><ul><li>Structure an app with multiple"
                " questions</li><li>Change questions and answers the DOM"
                " displays</li><li>Detect user input</li><li>Process correct and"
                " incorrect answers</li><li>Display scores and correct"
                " answers</li><li>Style the app’s appearance</li></ul>"
            ),
        },
        {
            "id": "4a71ec0b4831e122ac43f8dab9facb4196f22746",
            "type": "software",
            "name": "Create Your First Responsive Website",
            "edition": '<span class="callout-msrp">MSRP: $50<br></span>Web Development',
            "author": "",
            "publisher": "Zenva",
            "description": (
                "<p>Start your web development journey by building your first"
                " website!\xa0</p><p>Utilizing only basic HTML and CSS, you’ll master"
                " skills for combining the languages to create a company-styled website"
                " with navigation, banner, and grid-displayed services. You’ll also"
                " learn key techniques for responsively altering its appearance"
                " automatically based on screen size – a necessity in a mobile-first"
                " world! Not only will you create a project perfect for any portfolio,"
                " but also gain the foundations you’ll need as you dive further into"
                " web development!</p><p><strong>You will learn how"
                " to:</strong></p><ul><li>Lay out various webpage sections with"
                " HTML</li><li>Use Chrome Developer Tools to aid"
                " development</li><li>Create a navigation bar with hover"
                " effects</li><li>Display a splash banner</li><li>Showcase elements in"
                " a grid-style format</li><li>Set up CSS rules for different screen"
                " sizes</li></ul><p>… and more!</p>"
            ),
        },
        {
            "id": "8f47ce4debcd8d5f168eb796f4340afe45e9e12f",
            "type": "software",
            "name": "Responsive Admin Pages with Semantic UI",
            "edition": '<span class="callout-msrp">MSRP: $50<br></span>Web Development',
            "author": "",
            "publisher": "Zenva",
            "description": (
                '<p><span style="font-weight: 400;">This course will give you all you'
                " need to know to get started with Semantic UI – an open-source,"
                " lightweight, front-end framework featuring intuitive and"
                " easy-to-understand syntax. Powered by LESS and jQuery, a sound"
                " knowledge of Semantic UI can cut your development time in half"
                " through its extensive library of templates for widgets and page"
                " customizations. You'll also put your knowledge to use as you create"
                " a simulated e-commerce back-end, preparing you to build visually"
                " beautiful websites and apps.</span></p>\n<p><b>You will learn how"
                ' to:&nbsp;</b></p>\n<ul>\n<li style="font-weight: 400;"'
                ' aria-level="1"><span style="font-weight: 400;">Navigate the Semantic'
                " UI website and the different element themes</span></li>\n<li"
                ' style="font-weight: 400;" aria-level="1"><span style="font-weight:'
                ' 400;">Install Semantic UI</span></li>\n<li style="font-weight: 400;"'
                ' aria-level="1"><span style="font-weight: 400;">Copy and paste'
                " elements with themes into your code</span></li>\n<li"
                ' style="font-weight: 400;" aria-level="1"><span style="font-weight:'
                ' 400;">Customize page layouts using a Semantic UI'
                ' grid</span></li>\n<li style="font-weight: 400;" aria-level="1"><span'
                ' style="font-weight: 400;">Use Semantic UI widgets and'
                ' components</span></li>\n<li style="font-weight: 400;"'
                ' aria-level="1"><span style="font-weight: 400;">Further modify your'
                " elements using CSS</span></li>\n</ul>"
            ),
        },
        {
            "id": "89a245396fd7c2b31e2556a732c341d25f71c0c0",
            "type": "software",
            "name": "JavaScript Programming for Beginners",
            "edition": '<span class="callout-msrp">MSRP: $50<br></span>Web Development',
            "author": "",
            "publisher": "Zenva",
            "description": (
                "<p>Learn to code JavaScript – one of the most in-demand programming"
                " languages!</p><p>JavaScript is a lightweight scripting language that"
                " allows you to add dynamic, interactive content to your websites and"
                " apps. It also forms the foundation for some of the best development"
                " frameworks around, including React, Angular, and more.</p><p>You’ll"
                " learn JavaScript from scratch, starting with data storage and working"
                " up to altering webpages, and learn skills that can be expanded upon"
                " to develop any number of JavaScript programs!</p><p><strong>You will"
                " learn how to:</strong></p><ul><li>Store data as variables, arrays,"
                " and more</li><li>Manipulate data with operators</li><li>Evaluate data"
                " for specific actions</li><li>Control program logic and flow with"
                " functions, loops, and more</li><li>Set up objects to store complex"
                " sets of data</li><li>Alter webpages with the DOM API</li></ul><p>…"
                " and more!</p>"
            ),
        },
        {
            "id": "463fd56c713b4a14aeca21f2185a44fce41ed170",
            "type": "software",
            "name": "Bite-Sized Git and GitHub",
            "edition": '<span class="callout-msrp">MSRP: $50<br></span>Web Development',
            "author": "",
            "publisher": "Zenva",
            "description": (
                "<p>Version control enables you to manage different “versions” of a"
                " program, meaning you can make changes without fear of irreversible"
                " mistakes, and easily collaborate across teams.</p><p>You’ll explore"
                " how to manage your project versions using Git – a popular, free, and"
                " open-source version control system. Along with GitHub, a hosting"
                " platform for code built specifically for version control, you’ll"
                " learn to configure &amp; update your projects, control branches,"
                " collaborate, and more. Regardless of industry, these fundamentals"
                " will give you the in-demand skills needed for productive"
                " programming!\xa0</p><p><strong>You will learn how"
                " to:</strong></p><ul><li>Understand version control"
                " fundamentals</li><li>Configure projects for Git</li><li>Use Git"
                " commands for managing project versions</li><li>Incorporate your"
                " project into GitHub</li><li>Utilize GitHub’s collaboration"
                " tools</li></ul>"
            ),
        },
        {
            "id": "e43479227b7f9fad16e67b55af34dfd08dbced0f",
            "type": "software",
            "name": "Marker-Based Games with AR.js for Beginners",
            "edition": (
                '<span class="callout-msrp">MSRP: $50<br></span>Game Development -'
                " HTML5"
            ),
            "author": "",
            "publisher": "Zenva",
            "description": (
                "<p>Create unique AR experiences by mastering AR.js – a lightweight,"
                " open-source library for the web!</p><p>Based on A-Frame and Three.js,"
                " AR.js allows you to create AR apps that can be accessed on the web"
                " with any WebGL compatible device. Through this course, you’ll learn"
                " to build a marker-based jigsaw puzzle game that uses AR and image"
                " markers to display a custom picture. Not only will you get to explore"
                " the AR.js library and its features, but you’ll also develop skills"
                " with image markers and image tracking which can be applied to a wide"
                " variety of augmented reality projects!</p><p><strong>You will learn"
                " how to:</strong></p><ul><li>Understand AR</li><li>Set up AR.js for"
                " web projects</li><li>Implement image capturing</li><li>Slice images"
                " into pieces through code</li><li>Track image marker position and"
                " rotation</li><li>Detect win conditions based on marker"
                " images</li></ul><p>… and more!</p>"
            ),
        },
        {
            "id": "1a49cc68e771507c441f816ebf63eff60fb13ba0",
            "type": "software",
            "name": "Intro to Cloud Deployment with Heroku",
            "edition": (
                '<span class="callout-msrp">MSRP: $50<br></span>Game Development -'
                " HTML5"
            ),
            "author": "",
            "publisher": "Zenva",
            "description": (
                "<p>Learn to deploy a Phaser-made MMORPG to the cloud with Heroku. This"
                " platform as a service (PaaS) builds and operates your programs"
                " entirely on the cloud, and through this course, you’ll gain the"
                " skills needed to create a publicly accessible server – all while"
                " letting Heroku handle some of the backend server management for you."
                " Additionally, you’ll learn how to use MongoDB Atlas, another cloud"
                " service for deploying and managing your databases, to complete the"
                " deployment process for a seamless, multiplayer server"
                " setup.</p>\n<p><strong>You will learn how"
                " to:</strong></p>\n<ul>\n<li>Configure Heroku to deploy your"
                " game</li>\n<li>Set up a MongoDB cluster to store your"
                " database</li>\n<li>Update your code to work with Heroku and MongoDB"
                " Atlas</li>\n<li>Deploy your game to Heroku using Heroku’s"
                " CLI</li>\n<li>Test your deployment locally and over a"
                " server</li>\n</ul>"
            ),
        },
        {
            "id": "b2c91bdb83fb5ca6c0637f7ec6c2451bbe0cf6fe",
            "type": "software",
            "name": "Build 3D Web Apps with Babylon.js",
            "edition": (
                '<span class="callout-msrp">MSRP: $50<br></span>Game Development -'
                " HTML5"
            ),
            "author": "",
            "publisher": "Zenva",
            "description": (
                "<p>Bring 3D graphics to the web by mastering Babylon.js – a real-time,"
                " 3D render engine for HTML5 websites.</p><p>Based on WebGL, Babylon.js"
                " allows you to render static and animated 3D scenes using the HTML"
                " Canvas. Through this course, you'll explore using Babylon.js by"
                " building a solar system scene with planets that orbit around the sun."
                " Whether you want to create dynamic web-UIs, eye-catching showcases,"
                " or build an interactive scene, you will gain all the skills needed to"
                " build your 3D project right in your browser!</p><p><strong>You will"
                " learn how to:</strong></p><ul><li>Set up and test Babylon.js"
                " scenes</li><li>Implement simple and complex 3D"
                " objects</li><li>Manipulate 3D objects scaling, rotation, and"
                " position</li><li>Utilize materials to change object"
                " appearance</li><li>Adjust cameras and lighting</li><li>Animate 3D"
                " objects using only code</li></ul><p>… and more!</p>"
            ),
        },
        {
            "id": "0eda264d807e9fe8f55e823595914ddbcffd8cbd",
            "type": "software",
            "name": "Bite-Sized CSS Flexbox",
            "edition": '<span class="callout-msrp">MSRP: $50<br></span>Web Development',
            "author": "",
            "publisher": "Zenva",
            "description": (
                "<p>Enhance your responsive web development skills by learning CSS"
                " Flexbox. This one-dimensional, web layout model enables you to easily"
                " create dynamic layouts with elements that automatically resize, move,"
                " and more based on the device’s screen size. This course will show you"
                " how to utilize numerous aspects of CSS Flexbox – such as multiple"
                " column layouts, element positioning, and more – to build your own,"
                " professional-looking webpage with core skills perfect for many"
                " different web development projects.\xa0</p><p><strong>You will learn"
                " how to:</strong></p><ul><li>Understand the core features of CSS"
                " Flexbox</li><li>Set up CSS Flexbox for your web layout</li><li>Direct"
                " how elements increase or decrease in size</li><li>Dictate the"
                " direction, width, spacing, and more of Flexbox"
                " elements</li><li>Create a responsive web page with articles, footer,"
                " images, and more</li></ul>"
            ),
        },
        {
            "id": "b3a6a57589d2224608cbecca3d69d40c2fb659e6",
            "type": "software",
            "name": "PureCSS for Beginners",
            "edition": '<span class="callout-msrp">MSRP: $50<br></span>Web Development',
            "author": "",
            "publisher": "Zenva",
            "description": (
                "<p>Create beautiful websites quickly and easily by exploring PureCSS –"
                " a lightweight set of CSS modules for responsive web design. You’ll"
                " master techniques for creating web layouts, menus, forms, and more"
                " with pre-built CSS rules that you can implement in seconds. You’ll"
                " learn these methods by building the frontend for a messaging style"
                " app, cementing your knowledge with responsive design skills you can"
                " use for any future web projects!</p><p><strong>You will learn how"
                " to:</strong></p><ul><li>Install PureCSS to projects</li><li>Control"
                " layouts with grid modules</li><li>Create different style"
                " menus</li><li>Set up form fields and buttons</li><li>Utilize tables"
                " to create a calendar</li><li>Combine CSS rules to build a dynamic web"
                " UI</li></ul><p>… and more!</p>"
            ),
        },
        {
            "id": "8f1295dc77bac771f7b99d6b31deeb433ce3b70d",
            "type": "software",
            "name": "Intro to Frontend Development with React",
            "edition": '<span class="callout-msrp">MSRP: $50<br></span>Web Development',
            "author": "",
            "publisher": "Zenva",
            "description": (
                "<p>Build data-rich web apps by exploring React – a component-based"
                " JavaScript library!</p><p>Using React, you’ll learn how to render"
                " webpage UIs based on various pieces of data passed between"
                " components. You’ll explore these foundations while building an"
                " interactive shopping cart app from scratch. Not only will you master"
                " the tools and techniques made available by React, but you’ll also"
                " discover how to integrate them into the frontend of your own"
                " data-oriented web projects.</p><p><strong>You will learn how"
                " to:</strong></p><ul><li>Set up a web project with React</li><li>Use"
                " JavaScript XML (JSX) to write HTML elements in React</li><li>Create"
                " and style React components for dynamic UIs</li><li>Control how"
                " components render with states and Hooks</li><li>Send and receive data"
                " between components using “props”</li><li>Combine React foundations to"
                " build a shopping cart web app</li></ul>"
            ),
        },
        {
            "id": "974fac4e7598b58d8065239ce6eca40162956f7d",
            "type": "software",
            "name": "CSS Foundations",
            "edition": '<span class="callout-msrp">MSRP: $50<br></span>Web Development',
            "author": "",
            "publisher": "Zenva",
            "description": (
                "<p>Master website aesthetics and responsiveness by learning"
                " CSS.</p><p>CSS is a language geared at altering the appearance of"
                " markup languages. Whether you need to change margins, font styling,"
                " colors, or more, CSS allows you to design the aesthetics of your"
                " website across multiple pages. Further, CSS is the main driving force"
                " behind responsive design, as it allows developers to change layouts"
                " based on screen size.\xa0</p><p>This course will get you started with"
                " the basics of this powerful tool and provide you an in-demand set of"
                " skills to enhance the design of web projects.</p><p><strong>You will"
                " learn how to:</strong></p><ul><li>Import CSS into your web"
                " project</li><li>Select various HTML elements to"
                " alter</li><li>Position and size elements with CSS</li><li>Change"
                " colors and various stylings</li><li>Alter margins and"
                " padding</li><li>Adjust backgrounds, borders, text, and more</li></ul>"
            ),
        },
    ]
