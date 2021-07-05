FROM python:2.7
USER root
WORKDIR /root
ARG rootdir=/root
ARG wisdem=wisdem
ENV VIRTUAL_ENV=${rootdir}/jpnsecCompetition2019

RUN virtualenv -p python2.7 jpnsecCompetition2019
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN apt-get update \
    && apt-get install gfortran gcc python-dev python-tk git swig liblapack-dev -y
RUN pip install numpy scipy==0.17.1 algopy matplotlib pandas

RUN wget http://openmdao.org/releases/0.10.3.2/go-openmdao-0.10.3.2.py \
    && python go-openmdao-0.10.3.2.py

RUN mkdir ${wisdem}
RUN pip install -e git+https://github.com/WISDEM/akima.git@65c7c9be2b09170befe769bc26c0de2792139ad8#egg=akima
RUN pip install -e git+https://github.com/WISDEM/CommonSE.git@bb573cdc1be7a064c03ac446eb409ca683967657#egg=CommonSE
RUN pip install -e git+https://github.com/WISDEM/OffshoreBOS.git@8a5068fcee5e79785c50265d4dbb6d8c1fe801bf#egg=OffshoreBOS
RUN pip install -e git+https://github.com/WISDEM/NREL_CSM.git@94efc65a18659976f537b2c64ba126c36113ddf9#egg=nrel_csm
RUN cd ${wisdem} && git clone https://github.com/mdolab/pyoptsparse.git \
    && cd pyoptsparse \
    && git checkout c7c1f5af3814bc481303ffed980f4c3ad6be10a1 \
    && python setup.py install
RUN pip install -e git+https://github.com/WISDEM/pBeam.git@6e8d5169699da5c129d6728b0dd5207a53f07d53#egg=pBEAM
RUN pip install -e git+https://github.com/WISDEM/pyFrame3DD.git@147a60f5b31f5544c4dedbb2c8376ad45de85752#egg=pyFrame3DD
RUN pip install -e git+https://github.com/WISDEM/pyMAP.git@d63dd3882dcfb3d2d3b89bde56ba19d6fc88cb10#egg=pyMAP
RUN pip install -e git+https://github.com/WISDEM/DriveSE.git@f4f69c2fdb035e11f297e57ba9ac21556c5b11ec#egg=DriveSE
RUN pip install -e git+https://github.com/WISDEM/Plant_FinanceSE.git@8832c7b391e10fe9fc6a9139ea7e5fa17bb0d41f#egg=Plant_FinanceSE
RUN pip install -e git+https://github.com/WISDEM/TowerSE.git@b12faec307a3e08b9a3ef251a93ca4e43036f4b4#egg=TowerSE
RUN pip install -e git+https://github.com/WISDEM/Turbine_CostsSE.git@bfbb9f46340635cf5bcf38f4852f2f0e05b55153#egg=Turbine_CostsSE
RUN pip install -e git+https://github.com/WISDEM/DriveWPACT.git@d872163b9929ce54d7cec3814c3101809d2201b4#egg=DriveWPACT
RUN pip install -e git+https://github.com/WISDEM/Plant_CostsSE.git@c93c99fbb23a92c7222f15259bd3e204fb323407#egg=plant_costsse
RUN pip install -e git+https://github.com/WISDEM/Plant_EnergySE.git@5ca898bf65b63fd1a87a40241591866f5f0b185a#egg=Plant_EnergySE
RUN pip install -e git+https://github.com/WISDEM/AirfoilPreppy.git@43b44db4d262f2753d665522909bfde26cf4e51b#egg=AirfoilPrep-py
RUN pip install -e git+https://github.com/WISDEM/CCBlade.git@9654caa9c256dffa1984c09c8c67e6d0849123c3#egg=CCBlade
RUN pip install -e git+https://github.com/WISDEM/AirfoilPreppy.git@875093ed28ff418f22e1daba952472c932f9eb0d#egg=AirfoilPrep-py
RUN cd ${wisdem} \
    && git clone https://github.com/WISDEM/RotorSE.git \
    && cd RotorSE \
    && git checkout f044cc78f07cc5a8bafa8e5eadbf43faa70d9293 \
    && python setup.py build_ext --inplace \
    && python setup.py develop
RUN pip install -e git+https://github.com/OpenMDAO/OpenMDAO@2.9.1#egg=openmdao-2.9.1
RUN pip install -e git+https://github.com/WISDEM/FloatingSE.git@f13e0f38a7742ea00a8f446a9ebf505dcf7acd42#egg=FloatingSE
RUN cd ${wisdem} \
    && git clone https://github.com/WISDEM/WISDEM.git \
    && cd WISDEM \
    && git checkout aa3d679928aa5a93618cb8a60d5827db47ba6e76 \
    && python setup.py develop
RUN pip install -e git+https://github.com/FUSED-Wind/fusedwind.git#egg=fusedwind
RUN wget http://www.jpnsec.org/files/competition2019/data/dummies.zip \
    && unzip dummies \
    && cd dummies \
    && python setup.py install
RUN pip install -e git+https://github.com/WISDEM/pyFrame3DD.git@680a8ba1b00b45ad6f76a76374f2b83cfb3c56df#egg=pyFrame3DD
RUN pip install networkx==1.8.1
