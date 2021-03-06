	.data
eps:	.double	1e-1
two:	.double	2
	.text
	.global	gvqlen
gvqlen:
	movl	%esi,%eax
	pxor	%xmm1,%xmm1

loopd_gvl:
	cmpl	$2,%esi
	jl	loops_gvl
	decl	%esi
	decl	%esi

	movupd	(%ecx,%esi,8),%xmm0
	mulpd	%xmm0,%xmm0
	addpd	%xmm0,%xmm1

	jmp	loopd_gvl

loops_gvl:
	testl	%esi,%esi
	jz	end_gvl
	decl	%esi
	movsd	(%ecx),%xmm0
	addsd	%xmm0,%xmm1

end_gvl:
	haddpd	%xmm1,%xmm1

	movl	%eax,%esi
	retl

	.global	product
product:
	movl	%esi,%eax
	pxor	%xmm2,%xmm2

loopd_pr:
	cmpl	$2,%esi
	jl	loops_pr
	decl	%esi
	decl	%esi

	movupd	(%ebx,%esi,8),%xmm0
	movupd	(%edi,%esi,8),%xmm1
	mulpd	%xmm0,%xmm1
	addpd	%xmm1,%xmm2

	jmp	loopd_pr

loops_pr:
	testl	%esi,%esi
	jz	end_pr
	decl	%esi

	movsd	(%ebx),%xmm0
	movsd	(%edi),%xmm1
	mulsd	%xmm0,%xmm1
	addsd	%xmm1,%xmm2

end_pr:
	haddpd	%xmm2,%xmm2

	movl	%eax,%esi
	retl

	.global	gcompat
gcompat:
	pushl	%ebp
	movl	%esp,%ebp

	movl	%ebx,%ecx
	call	gvqlen
	movsd	%xmm1,%xmm5

	movl	%edi,%ecx
	call	gvqlen
	movsd	%xmm1,%xmm6

	call	product
	movsd	%xmm2,%xmm7

	movsd	two,%xmm0
	mulsd	%xmm0,%xmm7
	subsd	%xmm7,%xmm5
	addsd	%xmm6,%xmm5
	sqrtsd	%xmm5,%xmm5

	movl	%ebp,%esp
	popl	%ebp

	movsd	eps,%xmm0
	comisd	%xmm0,%xmm5
	ja	ncomp

	xorl	%esi,%esi
	incl	%esi
	jmp	end_gcomp

ncomp:
	xorl	%esi,%esi

end_gcomp:
	retl
